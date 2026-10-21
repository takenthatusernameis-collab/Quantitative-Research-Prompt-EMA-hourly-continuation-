# EMA Hourly Continuation — AAVE/USDT P89_144

**Symbol:** AAVE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7828 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0253 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.1587 |
| sortino_ratio | -0.2671 |
| max_drawdown | 0.2723 |
| cagr | -0.1156 |
| net_avg_win | 73.0174 |
| net_avg_loss | -96.9775 |
| avg_hold_time_bars | 7.8599 |
| exposure | 0.0918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
