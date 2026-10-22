# EMA Hourly Continuation — XTZ/USDT P50_200

**Symbol:** XTZ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6401 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -3.0521 |
| sortino_ratio | -0.8995 |
| max_drawdown | 0.6811 |
| cagr | -0.3479 |
| net_avg_win | 55.7529 |
| net_avg_loss | -80.9352 |
| avg_hold_time_bars | 19.5183 |
| exposure | 0.3868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
