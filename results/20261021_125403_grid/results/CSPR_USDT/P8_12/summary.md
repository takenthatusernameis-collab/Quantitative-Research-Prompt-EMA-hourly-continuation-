# EMA Hourly Continuation — CSPR/USDT P8_12

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8368 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -2.3505 |
| sortino_ratio | -0.5142 |
| max_drawdown | 0.4472 |
| cagr | -0.2102 |
| net_avg_win | 70.5685 |
| net_avg_loss | -91.9375 |
| avg_hold_time_bars | 4.6314 |
| exposure | 0.0497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
