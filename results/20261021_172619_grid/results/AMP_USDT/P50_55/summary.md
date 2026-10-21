# EMA Hourly Continuation — AMP/USDT P50_55

**Symbol:** AMP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.4083 |
| net_win_rate | 0.3729 |
| gross_profit_factor | 0.6195 |
| gross_win_rate | 0.3729 |
| sharpe_ratio | -3.7464 |
| sortino_ratio | -0.7117 |
| max_drawdown | 0.5776 |
| cagr | -0.2813 |
| net_avg_win | 58.9277 |
| net_avg_loss | -85.8221 |
| avg_hold_time_bars | 5.1299 |
| exposure | 0.0413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
