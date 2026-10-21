# EMA Hourly Continuation — GMX/USDT P8_100

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.7464 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -2.3174 |
| sortino_ratio | -0.7782 |
| max_drawdown | 0.6277 |
| cagr | -0.3006 |
| net_avg_win | 65.5724 |
| net_avg_loss | -80.3024 |
| avg_hold_time_bars | 24.4399 |
| exposure | 0.6188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
