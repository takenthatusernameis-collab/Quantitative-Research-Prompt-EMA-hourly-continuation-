# EMA Hourly Continuation — DCR/USDT P50_200

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -3.6267 |
| sortino_ratio | -1.0877 |
| max_drawdown | 0.7339 |
| cagr | -0.4013 |
| net_avg_win | 53.3326 |
| net_avg_loss | -73.6528 |
| avg_hold_time_bars | 17.3075 |
| exposure | 0.3540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
