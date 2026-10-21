# EMA Hourly Continuation — BAT/USDT P8_89

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.7959 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0150 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.6350 |
| sortino_ratio | -0.5510 |
| max_drawdown | 0.5246 |
| cagr | -0.2246 |
| net_avg_win | 65.9885 |
| net_avg_loss | -84.4231 |
| avg_hold_time_bars | 25.1863 |
| exposure | 0.6331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
