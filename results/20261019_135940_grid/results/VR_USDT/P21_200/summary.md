# EMA Hourly Continuation — VR/USDT P21_200

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.4726 |
| net_win_rate | 0.3265 |
| gross_profit_factor | 0.7164 |
| gross_win_rate | 0.3367 |
| sharpe_ratio | -8.6772 |
| sortino_ratio | -2.6751 |
| max_drawdown | 0.9811 |
| cagr | -0.7917 |
| net_avg_win | 54.9120 |
| net_avg_loss | -56.3378 |
| avg_hold_time_bars | 28.4163 |
| exposure | 0.6329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
