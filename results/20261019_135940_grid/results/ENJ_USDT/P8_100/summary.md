# EMA Hourly Continuation — ENJ/USDT P8_100

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6409 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -3.7970 |
| sortino_ratio | -1.3682 |
| max_drawdown | 0.8181 |
| cagr | -0.4819 |
| net_avg_win | 45.8813 |
| net_avg_loss | -64.9823 |
| avg_hold_time_bars | 22.5967 |
| exposure | 0.6769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
