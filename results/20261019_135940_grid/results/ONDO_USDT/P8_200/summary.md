# EMA Hourly Continuation — ONDO/USDT P8_200

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7135 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9652 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -2.4735 |
| sortino_ratio | -0.7634 |
| max_drawdown | 0.6135 |
| cagr | -0.3017 |
| net_avg_win | 64.3299 |
| net_avg_loss | -83.9566 |
| avg_hold_time_bars | 33.6520 |
| exposure | 0.7296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
