# EMA Hourly Continuation — NEO/USDT P8_55

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.6930 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -3.2573 |
| sortino_ratio | -1.2306 |
| max_drawdown | 0.7623 |
| cagr | -0.4305 |
| net_avg_win | 51.4671 |
| net_avg_loss | -66.8168 |
| avg_hold_time_bars | 14.2425 |
| exposure | 0.4538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
