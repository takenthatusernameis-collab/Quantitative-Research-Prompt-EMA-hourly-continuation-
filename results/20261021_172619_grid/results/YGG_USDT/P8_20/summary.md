# EMA Hourly Continuation — YGG/USDT P8_20

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.7703 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0440 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.5074 |
| sortino_ratio | -0.9293 |
| max_drawdown | 0.6888 |
| cagr | -0.3469 |
| net_avg_win | 65.5499 |
| net_avg_loss | -86.3735 |
| avg_hold_time_bars | 4.9776 |
| exposure | 0.1507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
