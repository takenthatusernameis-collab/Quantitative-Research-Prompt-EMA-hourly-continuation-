# EMA Hourly Continuation — MASK/USDT P21_200

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.5436 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -3.9132 |
| sortino_ratio | -1.1460 |
| max_drawdown | 0.7546 |
| cagr | -0.4235 |
| net_avg_win | 45.9923 |
| net_avg_loss | -68.1124 |
| avg_hold_time_bars | 30.5747 |
| exposure | 0.6045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
