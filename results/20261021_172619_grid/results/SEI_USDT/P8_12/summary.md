# EMA Hourly Continuation — SEI/USDT P8_12

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.7642 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0321 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.1900 |
| sortino_ratio | -0.2319 |
| max_drawdown | 0.2695 |
| cagr | -0.1012 |
| net_avg_win | 81.9398 |
| net_avg_loss | -109.5753 |
| avg_hold_time_bars | 5.4022 |
| exposure | 0.0452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
