# EMA Hourly Continuation — PHA/USDT P12_89

**Symbol:** PHA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.6278 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -4.1235 |
| sortino_ratio | -1.5793 |
| max_drawdown | 0.8588 |
| cagr | -0.5360 |
| net_avg_win | 40.8257 |
| net_avg_loss | -57.8269 |
| avg_hold_time_bars | 15.4493 |
| exposure | 0.5267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
