# EMA Hourly Continuation — SATS/USDT P21_100

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.6782 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -3.2934 |
| sortino_ratio | -1.1475 |
| max_drawdown | 0.7718 |
| cagr | -0.4186 |
| net_avg_win | 54.1691 |
| net_avg_loss | -71.4917 |
| avg_hold_time_bars | 14.4300 |
| exposure | 0.4009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
