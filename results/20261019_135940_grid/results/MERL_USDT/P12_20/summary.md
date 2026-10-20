# EMA Hourly Continuation — MERL/USDT P12_20

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1492 |
| net_profit_factor | 0.3605 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.6186 |
| gross_win_rate | 0.4229 |
| sharpe_ratio | -11.2465 |
| sortino_ratio | -6.1600 |
| max_drawdown | 0.9995 |
| cagr | -0.9513 |
| net_avg_win | 9.3280 |
| net_avg_loss | -17.6002 |
| avg_hold_time_bars | 2.4082 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
