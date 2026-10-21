# EMA Hourly Continuation — AMP/USDT P100_200

**Symbol:** AMP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.5206 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.6941 |
| gross_win_rate | 0.4125 |
| sharpe_ratio | -3.4535 |
| sortino_ratio | -0.8518 |
| max_drawdown | 0.6331 |
| cagr | -0.3266 |
| net_avg_win | 54.6928 |
| net_avg_loss | -73.7790 |
| avg_hold_time_bars | 14.0858 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
