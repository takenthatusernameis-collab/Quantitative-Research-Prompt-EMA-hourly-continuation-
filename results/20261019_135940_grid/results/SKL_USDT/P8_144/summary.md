# EMA Hourly Continuation — SKL/USDT P8_144

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7693 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0431 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.9959 |
| sortino_ratio | -0.6303 |
| max_drawdown | 0.5982 |
| cagr | -0.2561 |
| net_avg_win | 70.7863 |
| net_avg_loss | -92.0116 |
| avg_hold_time_bars | 33.8502 |
| exposure | 0.7601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
