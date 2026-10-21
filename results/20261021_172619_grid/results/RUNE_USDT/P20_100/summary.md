# EMA Hourly Continuation — RUNE/USDT P20_100

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8304 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0441 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.0467 |
| sortino_ratio | -0.2865 |
| max_drawdown | 0.3365 |
| cagr | -0.1251 |
| net_avg_win | 74.6777 |
| net_avg_loss | -95.5478 |
| avg_hold_time_bars | 31.6970 |
| exposure | 0.5230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
