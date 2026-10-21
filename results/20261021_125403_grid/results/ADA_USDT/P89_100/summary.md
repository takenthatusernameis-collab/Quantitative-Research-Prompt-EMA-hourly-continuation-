# EMA Hourly Continuation — ADA/USDT P89_100

**Symbol:** ADA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 82 |
| net_profit_factor | 0.7500 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0776 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.7449 |
| sortino_ratio | -0.0974 |
| max_drawdown | 0.1362 |
| cagr | -0.0438 |
| net_avg_win | 74.1337 |
| net_avg_loss | -108.9873 |
| avg_hold_time_bars | 4.3415 |
| exposure | 0.0162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
