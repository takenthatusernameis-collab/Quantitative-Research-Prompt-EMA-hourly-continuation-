# EMA Hourly Continuation — DYDX/USDT P20_21

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.7236 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0013 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1719 |
| sortino_ratio | -0.1963 |
| max_drawdown | 0.2135 |
| cagr | -0.0853 |
| net_avg_win | 77.2262 |
| net_avg_loss | -106.7257 |
| avg_hold_time_bars | 4.7500 |
| exposure | 0.0294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
