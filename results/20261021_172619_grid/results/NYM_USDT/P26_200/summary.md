# EMA Hourly Continuation — NYM/USDT P26_200

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.5433 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7355 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -3.0497 |
| sortino_ratio | -0.6829 |
| max_drawdown | 0.5589 |
| cagr | -0.2724 |
| net_avg_win | 62.9108 |
| net_avg_loss | -81.3756 |
| avg_hold_time_bars | 46.3929 |
| exposure | 0.5314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
