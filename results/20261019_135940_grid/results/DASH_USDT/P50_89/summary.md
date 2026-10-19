# EMA Hourly Continuation — DASH/USDT P50_89

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.3864 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -6.9342 |
| sortino_ratio | -2.5892 |
| max_drawdown | 0.9640 |
| cagr | -0.7255 |
| net_avg_win | 19.5247 |
| net_avg_loss | -39.9582 |
| avg_hold_time_bars | 4.2650 |
| exposure | 0.1361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
