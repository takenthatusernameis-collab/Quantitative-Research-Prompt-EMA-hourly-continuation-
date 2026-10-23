# EMA Hourly Continuation — LISTA/USDT P89_200

**Symbol:** LISTA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5811 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.8205 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -3.3591 |
| sortino_ratio | -0.9687 |
| max_drawdown | 0.6654 |
| cagr | -0.3694 |
| net_avg_win | 51.3627 |
| net_avg_loss | -73.8699 |
| avg_hold_time_bars | 10.2864 |
| exposure | 0.1967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
