# EMA Hourly Continuation — RAY/USDT P89_100

**Symbol:** RAY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1339 |
| sortino_ratio | -0.1852 |
| max_drawdown | 0.2350 |
| cagr | -0.0811 |
| net_avg_win | 75.9153 |
| net_avg_loss | -102.6243 |
| avg_hold_time_bars | 5.8154 |
| exposure | 0.0344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
