# EMA Hourly Continuation — CAKE/USDT P89_200

**Symbol:** CAKE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.5111 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -3.9794 |
| sortino_ratio | -1.0418 |
| max_drawdown | 0.7351 |
| cagr | -0.4066 |
| net_avg_win | 48.0298 |
| net_avg_loss | -76.6183 |
| avg_hold_time_bars | 9.9689 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
