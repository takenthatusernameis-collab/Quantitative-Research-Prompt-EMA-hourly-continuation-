# EMA Hourly Continuation — BIGTIME/USDT P12_50

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.6534 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9640 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -4.3123 |
| sortino_ratio | -1.9341 |
| max_drawdown | 0.8997 |
| cagr | -0.5971 |
| net_avg_win | 34.3719 |
| net_avg_loss | -50.6563 |
| avg_hold_time_bars | 7.5701 |
| exposure | 0.3443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
