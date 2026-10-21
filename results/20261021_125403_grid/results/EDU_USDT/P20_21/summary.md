# EMA Hourly Continuation — EDU/USDT P20_21

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.5277 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7711 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -2.8974 |
| sortino_ratio | -0.6432 |
| max_drawdown | 0.5279 |
| cagr | -0.2573 |
| net_avg_win | 54.6206 |
| net_avg_loss | -82.7989 |
| avg_hold_time_bars | 4.3786 |
| exposure | 0.0481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
