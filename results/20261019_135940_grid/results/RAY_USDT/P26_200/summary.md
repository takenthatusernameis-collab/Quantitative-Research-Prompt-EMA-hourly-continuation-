# EMA Hourly Continuation — RAY/USDT P26_200

**Symbol:** RAY/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6998 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9751 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -2.0513 |
| sortino_ratio | -0.5511 |
| max_drawdown | 0.5566 |
| cagr | -0.2295 |
| net_avg_win | 62.9353 |
| net_avg_loss | -86.5270 |
| avg_hold_time_bars | 34.1818 |
| exposure | 0.5640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
