# EMA Hourly Continuation — WEMIX/USDT P8_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.3402 |
| net_win_rate | 0.3362 |
| gross_profit_factor | 0.4957 |
| gross_win_rate | 0.3396 |
| sharpe_ratio | -8.0110 |
| sortino_ratio | -2.7295 |
| max_drawdown | 0.9673 |
| cagr | -0.7412 |
| net_avg_win | 25.1617 |
| net_avg_loss | -37.4590 |
| avg_hold_time_bars | 29.8353 |
| exposure | 0.7988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
