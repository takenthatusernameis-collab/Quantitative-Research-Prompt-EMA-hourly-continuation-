# EMA Hourly Continuation — BABYDOGE/USDT P21_26

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 12 |
| net_profit_factor | 1.2754 |
| net_win_rate | 0.5833 |
| gross_profit_factor | 1.3825 |
| gross_win_rate | 0.5833 |
| sharpe_ratio | 0.2766 |
| sortino_ratio | 0.0141 |
| max_drawdown | 0.0224 |
| cagr | 0.0058 |
| net_avg_win | 97.0520 |
| net_avg_loss | -106.5324 |
| avg_hold_time_bars | 13.3333 |
| exposure | 0.0072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
