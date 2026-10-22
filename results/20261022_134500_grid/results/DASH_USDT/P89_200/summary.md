# EMA Hourly Continuation — DASH/USDT P89_200

**Symbol:** DASH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.3321 |
| net_win_rate | 0.4105 |
| gross_profit_factor | 0.6984 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -5.7484 |
| sortino_ratio | -1.6992 |
| max_drawdown | 0.8922 |
| cagr | -0.5848 |
| net_avg_win | 23.5443 |
| net_avg_loss | -49.3584 |
| avg_hold_time_bars | 8.1812 |
| exposure | 0.1703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
