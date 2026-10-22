# EMA Hourly Continuation — EWT/USDT P21_100

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6680 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8184 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -2.5952 |
| sortino_ratio | -0.7941 |
| max_drawdown | 0.6294 |
| cagr | -0.3071 |
| net_avg_win | 56.8829 |
| net_avg_loss | -71.6857 |
| avg_hold_time_bars | 14.9850 |
| exposure | 0.3174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
