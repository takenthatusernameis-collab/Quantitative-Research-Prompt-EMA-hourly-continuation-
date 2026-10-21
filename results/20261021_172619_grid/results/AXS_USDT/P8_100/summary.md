# EMA Hourly Continuation — AXS/USDT P8_100

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.8845 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0786 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -0.7928 |
| sortino_ratio | -0.2444 |
| max_drawdown | 0.2900 |
| cagr | -0.1100 |
| net_avg_win | 80.9306 |
| net_avg_loss | -99.7806 |
| avg_hold_time_bars | 31.3398 |
| exposure | 0.6552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
