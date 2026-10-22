# EMA Hourly Continuation — ZPAY/USDT P26_50

**Symbol:** ZPAY/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.4038 |
| net_win_rate | 0.3300 |
| gross_profit_factor | 0.6284 |
| gross_win_rate | 0.3337 |
| sharpe_ratio | -8.9396 |
| sortino_ratio | -3.5574 |
| max_drawdown | 0.9866 |
| cagr | -0.8177 |
| net_avg_win | 25.0219 |
| net_avg_loss | -30.5244 |
| avg_hold_time_bars | 7.7157 |
| exposure | 0.2825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
