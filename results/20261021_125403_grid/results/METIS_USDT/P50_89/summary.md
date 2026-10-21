# EMA Hourly Continuation — METIS/USDT P50_89

**Symbol:** METIS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6835 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -2.1292 |
| sortino_ratio | -0.5518 |
| max_drawdown | 0.4860 |
| cagr | -0.2239 |
| net_avg_win | 64.7554 |
| net_avg_loss | -86.4822 |
| avg_hold_time_bars | 7.9544 |
| exposure | 0.1190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
