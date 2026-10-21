# EMA Hourly Continuation — HTX/USDT P34_50

**Symbol:** HTX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.2261 |
| net_win_rate | 0.2938 |
| gross_profit_factor | 0.4580 |
| gross_win_rate | 0.2997 |
| sharpe_ratio | -8.0372 |
| sortino_ratio | -2.1867 |
| max_drawdown | 0.9273 |
| cagr | -0.6462 |
| net_avg_win | 27.3587 |
| net_avg_loss | -50.3410 |
| avg_hold_time_bars | 6.5608 |
| exposure | 0.1001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
