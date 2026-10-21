# EMA Hourly Continuation — SHIB/USDT P20_50

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7259 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0186 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.3219 |
| sortino_ratio | -0.7083 |
| max_drawdown | 0.5951 |
| cagr | -0.2766 |
| net_avg_win | 65.5274 |
| net_avg_loss | -89.8663 |
| avg_hold_time_bars | 6.6341 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
