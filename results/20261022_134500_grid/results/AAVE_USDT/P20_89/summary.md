# EMA Hourly Continuation — AAVE/USDT P20_89

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.5299 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8303 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -4.9348 |
| sortino_ratio | -1.8113 |
| max_drawdown | 0.8983 |
| cagr | -0.5880 |
| net_avg_win | 31.7186 |
| net_avg_loss | -51.0108 |
| avg_hold_time_bars | 12.2134 |
| exposure | 0.3825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
