# EMA Hourly Continuation — GMT/USDT P21_200

**Symbol:** GMT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -1.0677 |
| sortino_ratio | -0.2555 |
| max_drawdown | 0.3174 |
| cagr | -0.1124 |
| net_avg_win | 73.9849 |
| net_avg_loss | -89.4882 |
| avg_hold_time_bars | 48.3986 |
| exposure | 0.6182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
