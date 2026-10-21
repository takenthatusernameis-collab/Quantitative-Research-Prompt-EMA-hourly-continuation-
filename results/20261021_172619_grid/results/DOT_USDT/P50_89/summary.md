# EMA Hourly Continuation — DOT/USDT P50_89

**Symbol:** DOT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1130 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -1.0209 |
| sortino_ratio | -0.2544 |
| max_drawdown | 0.2986 |
| cagr | -0.1109 |
| net_avg_win | 68.8839 |
| net_avg_loss | -96.6897 |
| avg_hold_time_bars | 7.7508 |
| exposure | 0.1046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
