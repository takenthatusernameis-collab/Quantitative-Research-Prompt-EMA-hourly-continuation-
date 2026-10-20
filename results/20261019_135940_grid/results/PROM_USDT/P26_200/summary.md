# EMA Hourly Continuation — PROM/USDT P26_200

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.4294 |
| net_win_rate | 0.3933 |
| gross_profit_factor | 0.6793 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -5.6329 |
| sortino_ratio | -1.7175 |
| max_drawdown | 0.8895 |
| cagr | -0.5707 |
| net_avg_win | 35.2389 |
| net_avg_loss | -53.2035 |
| avg_hold_time_bars | 24.5272 |
| exposure | 0.5329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
