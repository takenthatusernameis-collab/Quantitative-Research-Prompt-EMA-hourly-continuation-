# EMA Hourly Continuation — IMX/USDT P26_144

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.9096 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.0777 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -0.4498 |
| sortino_ratio | -0.1226 |
| max_drawdown | 0.2441 |
| cagr | -0.0590 |
| net_avg_win | 76.0824 |
| net_avg_loss | -91.4285 |
| avg_hold_time_bars | 30.4917 |
| exposure | 0.4967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
