# EMA Hourly Continuation — ONE/USDT P26_200

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.8877 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0385 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -0.6307 |
| sortino_ratio | -0.1518 |
| max_drawdown | 0.2577 |
| cagr | -0.0700 |
| net_avg_win | 91.4877 |
| net_avg_loss | -107.5432 |
| avg_hold_time_bars | 48.5177 |
| exposure | 0.6219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
