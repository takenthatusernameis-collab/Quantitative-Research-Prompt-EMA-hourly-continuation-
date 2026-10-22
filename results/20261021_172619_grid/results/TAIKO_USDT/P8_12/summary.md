# EMA Hourly Continuation — TAIKO/USDT P8_12

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.8641 |
| net_win_rate | 0.5683 |
| gross_profit_factor | 1.3084 |
| gross_win_rate | 0.5683 |
| sharpe_ratio | -0.7737 |
| sortino_ratio | -0.1905 |
| max_drawdown | 0.3280 |
| cagr | -0.0847 |
| net_avg_win | 78.2819 |
| net_avg_loss | -119.2486 |
| avg_hold_time_bars | 5.2768 |
| exposure | 0.0687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
