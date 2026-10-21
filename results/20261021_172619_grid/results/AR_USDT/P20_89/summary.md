# EMA Hourly Continuation — AR/USDT P20_89

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7461 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -1.9974 |
| sortino_ratio | -0.6408 |
| max_drawdown | 0.5459 |
| cagr | -0.2565 |
| net_avg_win | 63.4880 |
| net_avg_loss | -78.3209 |
| avg_hold_time_bars | 15.2623 |
| exposure | 0.3517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
