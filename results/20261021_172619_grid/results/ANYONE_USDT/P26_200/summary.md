# EMA Hourly Continuation — ANYONE/USDT P26_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.8155 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.0023 |
| sortino_ratio | -0.2280 |
| max_drawdown | 0.3032 |
| cagr | -0.1015 |
| net_avg_win | 85.5081 |
| net_avg_loss | -96.9940 |
| avg_hold_time_bars | 52.8225 |
| exposure | 0.6166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
