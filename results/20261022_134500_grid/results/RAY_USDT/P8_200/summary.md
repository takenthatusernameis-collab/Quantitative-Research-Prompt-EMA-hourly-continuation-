# EMA Hourly Continuation — RAY/USDT P8_200

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7369 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9727 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -2.1772 |
| sortino_ratio | -0.6451 |
| max_drawdown | 0.5663 |
| cagr | -0.2639 |
| net_avg_win | 69.5975 |
| net_avg_loss | -89.8714 |
| avg_hold_time_bars | 37.9300 |
| exposure | 0.7638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
