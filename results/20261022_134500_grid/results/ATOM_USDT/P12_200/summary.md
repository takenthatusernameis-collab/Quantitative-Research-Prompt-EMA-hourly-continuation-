# EMA Hourly Continuation — ATOM/USDT P12_200

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.6299 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9304 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.8320 |
| sortino_ratio | -0.7873 |
| max_drawdown | 0.6363 |
| cagr | -0.3196 |
| net_avg_win | 55.2254 |
| net_avg_loss | -81.2910 |
| avg_hold_time_bars | 39.9647 |
| exposure | 0.7212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
