# EMA Hourly Continuation — ETN/USDT P50_55

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.1414 |
| net_win_rate | 0.2342 |
| gross_profit_factor | 0.3345 |
| gross_win_rate | 0.2820 |
| sharpe_ratio | -16.2738 |
| sortino_ratio | -7.4190 |
| max_drawdown | 0.9998 |
| cagr | -0.9839 |
| net_avg_win | 9.0958 |
| net_avg_loss | -19.6700 |
| avg_hold_time_bars | 2.1307 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
