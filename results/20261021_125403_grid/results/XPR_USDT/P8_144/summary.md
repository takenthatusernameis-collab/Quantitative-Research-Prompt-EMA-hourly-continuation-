# EMA Hourly Continuation — XPR/USDT P8_144

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.8515 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0253 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -0.8899 |
| sortino_ratio | -0.2535 |
| max_drawdown | 0.3086 |
| cagr | -0.1123 |
| net_avg_win | 73.7512 |
| net_avg_loss | -90.2086 |
| avg_hold_time_bars | 36.6599 |
| exposure | 0.6565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
