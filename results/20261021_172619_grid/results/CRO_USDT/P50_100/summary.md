# EMA Hourly Continuation — CRO/USDT P50_100

**Symbol:** CRO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6920 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -2.0541 |
| sortino_ratio | -0.5407 |
| max_drawdown | 0.5052 |
| cagr | -0.2187 |
| net_avg_win | 61.4061 |
| net_avg_loss | -90.3433 |
| avg_hold_time_bars | 9.8537 |
| exposure | 0.1500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
