# EMA Hourly Continuation — AXL/USDT P55_144

**Symbol:** AXL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7079 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.2694 |
| sortino_ratio | -0.6688 |
| max_drawdown | 0.5734 |
| cagr | -0.2653 |
| net_avg_win | 64.8445 |
| net_avg_loss | -80.8033 |
| avg_hold_time_bars | 12.0464 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
