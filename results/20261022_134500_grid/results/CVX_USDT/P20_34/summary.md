# EMA Hourly Continuation — CVX/USDT P20_34

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.3828 |
| net_win_rate | 0.4216 |
| gross_profit_factor | 0.7714 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -9.8699 |
| sortino_ratio | -4.7481 |
| max_drawdown | 0.9973 |
| cagr | -0.9053 |
| net_avg_win | 12.7811 |
| net_avg_loss | -24.3361 |
| avg_hold_time_bars | 2.8406 |
| exposure | 0.1482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
