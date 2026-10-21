# EMA Hourly Continuation — CTC/USDT P50_89

**Symbol:** CTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.5650 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8315 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -3.1319 |
| sortino_ratio | -0.8289 |
| max_drawdown | 0.6243 |
| cagr | -0.3179 |
| net_avg_win | 50.7591 |
| net_avg_loss | -76.7262 |
| avg_hold_time_bars | 8.4111 |
| exposure | 0.1311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
