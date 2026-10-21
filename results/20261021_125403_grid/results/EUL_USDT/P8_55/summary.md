# EMA Hourly Continuation — EUL/USDT P8_55

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.7612 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.9593 |
| sortino_ratio | -0.7147 |
| max_drawdown | 0.6018 |
| cagr | -0.2812 |
| net_avg_win | 56.1470 |
| net_avg_loss | -71.0915 |
| avg_hold_time_bars | 15.7868 |
| exposure | 0.4679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
