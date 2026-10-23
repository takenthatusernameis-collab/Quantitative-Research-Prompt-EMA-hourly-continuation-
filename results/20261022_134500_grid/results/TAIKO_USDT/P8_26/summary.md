# EMA Hourly Continuation — TAIKO/USDT P8_26

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1415 |
| net_profit_factor | 0.5248 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.9346 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -10.2692 |
| sortino_ratio | -5.5754 |
| max_drawdown | 0.9988 |
| cagr | -0.9400 |
| net_avg_win | 17.7074 |
| net_avg_loss | -26.5394 |
| avg_hold_time_bars | 4.2615 |
| exposure | 0.2897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
