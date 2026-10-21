# EMA Hourly Continuation — ZIL/USDT P12_34

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -3.2063 |
| sortino_ratio | -1.1395 |
| max_drawdown | 0.7478 |
| cagr | -0.4056 |
| net_avg_win | 52.2450 |
| net_avg_loss | -72.3435 |
| avg_hold_time_bars | 6.6124 |
| exposure | 0.1845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
