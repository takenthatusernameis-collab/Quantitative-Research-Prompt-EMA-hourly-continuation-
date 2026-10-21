# EMA Hourly Continuation — ID/USDT P21_50

**Symbol:** ID/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.7138 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9978 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -2.5895 |
| sortino_ratio | -0.8922 |
| max_drawdown | 0.6510 |
| cagr | -0.3352 |
| net_avg_win | 55.4815 |
| net_avg_loss | -77.1950 |
| avg_hold_time_bars | 7.6483 |
| exposure | 0.2008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
