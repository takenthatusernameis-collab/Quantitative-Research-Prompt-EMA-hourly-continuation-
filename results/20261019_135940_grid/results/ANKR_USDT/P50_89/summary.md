# EMA Hourly Continuation — ANKR/USDT P50_89

**Symbol:** ANKR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.4255 |
| net_win_rate | 0.4083 |
| gross_profit_factor | 0.7885 |
| gross_win_rate | 0.4334 |
| sharpe_ratio | -7.5492 |
| sortino_ratio | -2.7901 |
| max_drawdown | 0.9683 |
| cagr | -0.7451 |
| net_avg_win | 25.9696 |
| net_avg_loss | -42.1116 |
| avg_hold_time_bars | 6.6287 |
| exposure | 0.2037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
