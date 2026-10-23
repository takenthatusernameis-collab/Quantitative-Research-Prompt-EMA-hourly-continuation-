# EMA Hourly Continuation — BICO/USDT P144_200

**Symbol:** BICO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.5158 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -3.9697 |
| sortino_ratio | -1.0667 |
| max_drawdown | 0.7221 |
| cagr | -0.3994 |
| net_avg_win | 48.3700 |
| net_avg_loss | -73.8190 |
| avg_hold_time_bars | 6.3019 |
| exposure | 0.1034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
