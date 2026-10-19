# EMA Hourly Continuation — ETC/USDT P21_200

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -3.5994 |
| sortino_ratio | -0.9752 |
| max_drawdown | 0.7153 |
| cagr | -0.3853 |
| net_avg_win | 53.0120 |
| net_avg_loss | -81.2331 |
| avg_hold_time_bars | 36.0236 |
| exposure | 0.6239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
