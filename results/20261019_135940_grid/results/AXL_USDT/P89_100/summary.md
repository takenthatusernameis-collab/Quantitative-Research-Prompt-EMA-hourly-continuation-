# EMA Hourly Continuation — AXL/USDT P89_100

**Symbol:** AXL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.3542 |
| net_win_rate | 0.3806 |
| gross_profit_factor | 0.8689 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -9.5353 |
| sortino_ratio | -3.6703 |
| max_drawdown | 0.9904 |
| cagr | -0.8406 |
| net_avg_win | 20.0419 |
| net_avg_loss | -34.7711 |
| avg_hold_time_bars | 2.4003 |
| exposure | 0.0773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
