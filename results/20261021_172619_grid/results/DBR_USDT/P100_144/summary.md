# EMA Hourly Continuation — DBR/USDT P100_144

**Symbol:** DBR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.5167 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.7946 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -2.8299 |
| sortino_ratio | -0.5936 |
| max_drawdown | 0.4406 |
| cagr | -0.2390 |
| net_avg_win | 57.8550 |
| net_avg_loss | -91.9305 |
| avg_hold_time_bars | 16.2832 |
| exposure | 0.1602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
