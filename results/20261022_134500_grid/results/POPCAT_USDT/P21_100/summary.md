# EMA Hourly Continuation — POPCAT/USDT P21_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.5075 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.6841 |
| gross_win_rate | 0.4172 |
| sharpe_ratio | -5.5044 |
| sortino_ratio | -2.0389 |
| max_drawdown | 0.8835 |
| cagr | -0.6266 |
| net_avg_win | 36.1733 |
| net_avg_loss | -50.6788 |
| avg_hold_time_bars | 13.2682 |
| exposure | 0.4233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
