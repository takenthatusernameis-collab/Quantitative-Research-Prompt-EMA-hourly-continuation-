# EMA Hourly Continuation — BIGTIME/USDT P21_26

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1187 |
| net_profit_factor | 0.2783 |
| net_win_rate | 0.3741 |
| gross_profit_factor | 0.6897 |
| gross_win_rate | 0.4238 |
| sharpe_ratio | -12.9081 |
| sortino_ratio | -6.3756 |
| max_drawdown | 0.9998 |
| cagr | -0.9627 |
| net_avg_win | 8.6835 |
| net_avg_loss | -18.6447 |
| avg_hold_time_bars | 2.4339 |
| exposure | 0.1307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
