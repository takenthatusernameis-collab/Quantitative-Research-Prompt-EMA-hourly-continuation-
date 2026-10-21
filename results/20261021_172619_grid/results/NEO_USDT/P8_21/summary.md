# EMA Hourly Continuation — NEO/USDT P8_21

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.5199 |
| gross_profit_factor | 1.0500 |
| gross_win_rate | 0.5199 |
| sharpe_ratio | -2.4487 |
| sortino_ratio | -0.8507 |
| max_drawdown | 0.6370 |
| cagr | -0.3195 |
| net_avg_win | 49.9337 |
| net_avg_loss | -76.3549 |
| avg_hold_time_bars | 5.8774 |
| exposure | 0.1547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
