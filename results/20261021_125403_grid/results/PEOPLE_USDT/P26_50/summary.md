# EMA Hourly Continuation — PEOPLE/USDT P26_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6756 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.5629 |
| sortino_ratio | -0.7807 |
| max_drawdown | 0.5990 |
| cagr | -0.3000 |
| net_avg_win | 56.4240 |
| net_avg_loss | -77.1764 |
| avg_hold_time_bars | 6.2478 |
| exposure | 0.1289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
