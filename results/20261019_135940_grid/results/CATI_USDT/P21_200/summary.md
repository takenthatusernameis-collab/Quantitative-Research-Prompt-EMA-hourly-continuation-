# EMA Hourly Continuation — CATI/USDT P21_200

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.4969 |
| net_win_rate | 0.4088 |
| gross_profit_factor | 0.7565 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -4.7073 |
| sortino_ratio | -1.3675 |
| max_drawdown | 0.7766 |
| cagr | -0.4893 |
| net_avg_win | 50.2601 |
| net_avg_loss | -69.9593 |
| avg_hold_time_bars | 33.1934 |
| exposure | 0.6587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
