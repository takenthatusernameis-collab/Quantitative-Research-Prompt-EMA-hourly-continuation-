# EMA Hourly Continuation — ALEX/USDT P21_200

**Symbol:** ALEX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.6165 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -2.7892 |
| sortino_ratio | -0.6858 |
| max_drawdown | 0.5831 |
| cagr | -0.2769 |
| net_avg_win | 66.8195 |
| net_avg_loss | -84.4377 |
| avg_hold_time_bars | 49.4020 |
| exposure | 0.6871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
