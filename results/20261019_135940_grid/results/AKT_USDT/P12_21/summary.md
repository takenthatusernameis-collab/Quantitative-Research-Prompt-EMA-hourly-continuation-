# EMA Hourly Continuation — AKT/USDT P12_21

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1368 |
| net_profit_factor | 0.4210 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.9889 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -12.3213 |
| sortino_ratio | -6.4462 |
| max_drawdown | 0.9998 |
| cagr | -0.9644 |
| net_avg_win | 13.1919 |
| net_avg_loss | -21.1339 |
| avg_hold_time_bars | 2.2193 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
