# EMA Hourly Continuation — RSR/USDT P20_34

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.6862 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9085 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -2.1463 |
| sortino_ratio | -0.5608 |
| max_drawdown | 0.5144 |
| cagr | -0.2268 |
| net_avg_win | 65.0263 |
| net_avg_loss | -87.1377 |
| avg_hold_time_bars | 5.7186 |
| exposure | 0.0868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
