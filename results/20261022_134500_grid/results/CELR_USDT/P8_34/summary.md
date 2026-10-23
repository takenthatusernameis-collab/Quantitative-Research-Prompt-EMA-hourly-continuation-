# EMA Hourly Continuation — CELR/USDT P8_34

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1340 |
| net_profit_factor | 0.4678 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -8.3402 |
| sortino_ratio | -4.2955 |
| max_drawdown | 0.9947 |
| cagr | -0.8741 |
| net_avg_win | 14.9695 |
| net_avg_loss | -24.7203 |
| avg_hold_time_bars | 5.8754 |
| exposure | 0.3563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
