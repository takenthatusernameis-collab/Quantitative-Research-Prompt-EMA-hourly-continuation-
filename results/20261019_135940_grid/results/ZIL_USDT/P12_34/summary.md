# EMA Hourly Continuation — ZIL/USDT P12_34

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.3859 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.8505 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -10.2387 |
| sortino_ratio | -5.2002 |
| max_drawdown | 0.9987 |
| cagr | -0.9271 |
| net_avg_win | 11.3454 |
| net_avg_loss | -21.9138 |
| avg_hold_time_bars | 4.0324 |
| exposure | 0.2374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
