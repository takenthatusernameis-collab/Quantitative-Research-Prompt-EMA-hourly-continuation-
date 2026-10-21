# EMA Hourly Continuation — DASH/USDT P21_34

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.6271 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.2130 |
| sortino_ratio | -0.5066 |
| max_drawdown | 0.4627 |
| cagr | -0.2066 |
| net_avg_win | 60.7619 |
| net_avg_loss | -88.8824 |
| avg_hold_time_bars | 5.4627 |
| exposure | 0.0633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
