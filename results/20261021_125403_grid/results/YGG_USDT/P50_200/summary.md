# EMA Hourly Continuation — YGG/USDT P50_200

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8604 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0161 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -0.7621 |
| sortino_ratio | -0.1849 |
| max_drawdown | 0.3114 |
| cagr | -0.0841 |
| net_avg_win | 83.8715 |
| net_avg_loss | -100.2248 |
| avg_hold_time_bars | 29.8090 |
| exposure | 0.3885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
