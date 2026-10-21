# EMA Hourly Continuation — AKT/USDT P26_100

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.8478 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0273 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.0326 |
| sortino_ratio | -0.3108 |
| max_drawdown | 0.3249 |
| cagr | -0.1358 |
| net_avg_win | 76.3045 |
| net_avg_loss | -93.3370 |
| avg_hold_time_bars | 14.8136 |
| exposure | 0.2963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
