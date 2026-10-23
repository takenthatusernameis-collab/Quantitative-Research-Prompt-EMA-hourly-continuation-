# EMA Hourly Continuation — PIXEL/USDT P21_50

**Symbol:** PIXEL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.5587 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -5.7569 |
| sortino_ratio | -2.5217 |
| max_drawdown | 0.9556 |
| cagr | -0.7032 |
| net_avg_win | 26.5221 |
| net_avg_loss | -42.0250 |
| avg_hold_time_bars | 5.2147 |
| exposure | 0.2287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
