# EMA Hourly Continuation — AKT/USDT P12_20

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.7327 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9816 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.4511 |
| sortino_ratio | -0.3192 |
| max_drawdown | 0.3789 |
| cagr | -0.1361 |
| net_avg_win | 72.0188 |
| net_avg_loss | -97.4610 |
| avg_hold_time_bars | 4.9787 |
| exposure | 0.0532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
