# EMA Hourly Continuation — MINA/USDT P89_200

**Symbol:** MINA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7376 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0629 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -1.6341 |
| sortino_ratio | -0.4421 |
| max_drawdown | 0.4360 |
| cagr | -0.1861 |
| net_avg_win | 61.3581 |
| net_avg_loss | -89.9980 |
| avg_hold_time_bars | 14.3596 |
| exposure | 0.2324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
