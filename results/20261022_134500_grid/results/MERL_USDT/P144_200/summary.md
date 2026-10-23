# EMA Hourly Continuation — MERL/USDT P144_200

**Symbol:** MERL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.5382 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.8255 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -3.9703 |
| sortino_ratio | -1.0584 |
| max_drawdown | 0.7493 |
| cagr | -0.4083 |
| net_avg_win | 53.9460 |
| net_avg_loss | -76.8782 |
| avg_hold_time_bars | 5.0824 |
| exposure | 0.0843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
