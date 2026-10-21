# EMA Hourly Continuation — LDO/USDT P8_200

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.7171 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -1.4183 |
| sortino_ratio | -0.2945 |
| max_drawdown | 0.3309 |
| cagr | -0.1273 |
| net_avg_win | 74.8994 |
| net_avg_loss | -86.7437 |
| avg_hold_time_bars | 86.6620 |
| exposure | 0.8509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
