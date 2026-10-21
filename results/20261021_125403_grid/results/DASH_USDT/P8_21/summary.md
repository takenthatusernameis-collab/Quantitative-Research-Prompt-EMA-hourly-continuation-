# EMA Hourly Continuation — DASH/USDT P8_21

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0611 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.9551 |
| sortino_ratio | -0.6392 |
| max_drawdown | 0.5596 |
| cagr | -0.2540 |
| net_avg_win | 57.1344 |
| net_avg_loss | -81.9524 |
| avg_hold_time_bars | 5.7126 |
| exposure | 0.1337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
