# EMA Hourly Continuation — COTI/USDT P8_100

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.7282 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0393 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -2.6831 |
| sortino_ratio | -1.0276 |
| max_drawdown | 0.7374 |
| cagr | -0.3891 |
| net_avg_win | 50.8544 |
| net_avg_loss | -71.3618 |
| avg_hold_time_bars | 19.5581 |
| exposure | 0.6579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
