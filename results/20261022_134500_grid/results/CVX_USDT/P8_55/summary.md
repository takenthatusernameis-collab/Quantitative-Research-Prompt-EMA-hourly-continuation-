# EMA Hourly Continuation — CVX/USDT P8_55

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.5418 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.7997 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -5.7913 |
| sortino_ratio | -2.6336 |
| max_drawdown | 0.9585 |
| cagr | -0.7165 |
| net_avg_win | 24.0503 |
| net_avg_loss | -36.3582 |
| avg_hold_time_bars | 10.4465 |
| exposure | 0.4967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
