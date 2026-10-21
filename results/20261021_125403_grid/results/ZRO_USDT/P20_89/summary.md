# EMA Hourly Continuation — ZRO/USDT P20_89

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.9001 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0627 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.6821 |
| sortino_ratio | -0.2188 |
| max_drawdown | 0.2547 |
| cagr | -0.1005 |
| net_avg_win | 82.5243 |
| net_avg_loss | -98.2601 |
| avg_hold_time_bars | 16.0346 |
| exposure | 0.3626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
