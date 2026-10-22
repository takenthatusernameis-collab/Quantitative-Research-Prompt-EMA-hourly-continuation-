# EMA Hourly Continuation — GTC/USDT P21_89

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7790 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -1.7871 |
| sortino_ratio | -0.5854 |
| max_drawdown | 0.5338 |
| cagr | -0.2371 |
| net_avg_win | 66.6208 |
| net_avg_loss | -84.5443 |
| avg_hold_time_bars | 14.7410 |
| exposure | 0.3518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
