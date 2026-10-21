# EMA Hourly Continuation — HTX/USDT P50_89

**Symbol:** HTX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.3864 |
| net_win_rate | 0.3509 |
| gross_profit_factor | 0.6889 |
| gross_win_rate | 0.3559 |
| sharpe_ratio | -7.2360 |
| sortino_ratio | -2.1015 |
| max_drawdown | 0.9230 |
| cagr | -0.6356 |
| net_avg_win | 41.4479 |
| net_avg_loss | -57.9888 |
| avg_hold_time_bars | 8.5965 |
| exposure | 0.1552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
