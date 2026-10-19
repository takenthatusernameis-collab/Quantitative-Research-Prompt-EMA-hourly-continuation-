# EMA Hourly Continuation — TWT/USDT P89_200

**Symbol:** TWT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.4958 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -4.1186 |
| sortino_ratio | -1.1808 |
| max_drawdown | 0.7669 |
| cagr | -0.4293 |
| net_avg_win | 39.7306 |
| net_avg_loss | -67.4974 |
| avg_hold_time_bars | 10.7653 |
| exposure | 0.2001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
