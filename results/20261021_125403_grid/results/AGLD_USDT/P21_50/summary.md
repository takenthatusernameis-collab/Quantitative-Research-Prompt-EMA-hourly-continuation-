# EMA Hourly Continuation — AGLD/USDT P21_50

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.9069 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -3.6535 |
| sortino_ratio | -1.3180 |
| max_drawdown | 0.8116 |
| cagr | -0.4543 |
| net_avg_win | 54.6412 |
| net_avg_loss | -69.5322 |
| avg_hold_time_bars | 7.4806 |
| exposure | 0.2177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
