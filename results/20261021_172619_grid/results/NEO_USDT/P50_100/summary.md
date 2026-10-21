# EMA Hourly Continuation — NEO/USDT P50_100

**Symbol:** NEO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.6356 |
| sortino_ratio | -0.7411 |
| max_drawdown | 0.5963 |
| cagr | -0.2885 |
| net_avg_win | 55.9380 |
| net_avg_loss | -80.3500 |
| avg_hold_time_bars | 9.1085 |
| exposure | 0.1602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
