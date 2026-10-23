# EMA Hourly Continuation — ETN/USDT P21_100

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.4166 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.6341 |
| gross_win_rate | 0.3912 |
| sharpe_ratio | -8.2194 |
| sortino_ratio | -3.2979 |
| max_drawdown | 0.9679 |
| cagr | -0.8026 |
| net_avg_win | 26.5582 |
| net_avg_loss | -38.9994 |
| avg_hold_time_bars | 10.0394 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
