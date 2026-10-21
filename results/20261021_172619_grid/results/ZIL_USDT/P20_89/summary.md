# EMA Hourly Continuation — ZIL/USDT P20_89

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.8256 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0860 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -1.4488 |
| sortino_ratio | -0.4617 |
| max_drawdown | 0.5072 |
| cagr | -0.1921 |
| net_avg_win | 77.3301 |
| net_avg_loss | -100.3792 |
| avg_hold_time_bars | 15.4582 |
| exposure | 0.3450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
