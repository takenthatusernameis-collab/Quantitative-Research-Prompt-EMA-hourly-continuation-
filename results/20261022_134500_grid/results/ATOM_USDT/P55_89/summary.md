# EMA Hourly Continuation — ATOM/USDT P55_89

**Symbol:** ATOM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.4638 |
| net_win_rate | 0.4992 |
| gross_profit_factor | 0.9884 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -5.0191 |
| sortino_ratio | -1.7364 |
| max_drawdown | 0.8863 |
| cagr | -0.5765 |
| net_avg_win | 25.3314 |
| net_avg_loss | -54.4357 |
| avg_hold_time_bars | 4.0215 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
