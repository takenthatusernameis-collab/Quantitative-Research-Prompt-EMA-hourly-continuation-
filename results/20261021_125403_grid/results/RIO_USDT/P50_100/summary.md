# EMA Hourly Continuation — RIO/USDT P50_100

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6767 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.7929 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -2.3443 |
| sortino_ratio | -0.6020 |
| max_drawdown | 0.5213 |
| cagr | -0.2426 |
| net_avg_win | 73.0181 |
| net_avg_loss | -83.8637 |
| avg_hold_time_bars | 7.8410 |
| exposure | 0.1177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
