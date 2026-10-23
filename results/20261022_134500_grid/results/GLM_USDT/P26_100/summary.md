# EMA Hourly Continuation — GLM/USDT P26_100

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -5.0056 |
| sortino_ratio | -1.8329 |
| max_drawdown | 0.8914 |
| cagr | -0.5835 |
| net_avg_win | 32.3130 |
| net_avg_loss | -50.7168 |
| avg_hold_time_bars | 11.5944 |
| exposure | 0.3547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
