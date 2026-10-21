# EMA Hourly Continuation — CRO/USDT P89_100

**Symbol:** CRO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 106 |
| net_profit_factor | 0.6692 |
| net_win_rate | 0.5189 |
| gross_profit_factor | 1.0639 |
| gross_win_rate | 0.5189 |
| sharpe_ratio | -1.2370 |
| sortino_ratio | -0.1839 |
| max_drawdown | 0.2369 |
| cagr | -0.0806 |
| net_avg_win | 69.9512 |
| net_avg_loss | -112.7327 |
| avg_hold_time_bars | 5.0660 |
| exposure | 0.0244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
