# EMA Hourly Continuation — XRP/USDT P26_200

**Symbol:** XRP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.5137 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.9251 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -4.0515 |
| sortino_ratio | -1.1585 |
| max_drawdown | 0.7683 |
| cagr | -0.4371 |
| net_avg_win | 41.1570 |
| net_avg_loss | -69.4900 |
| avg_hold_time_bars | 29.4171 |
| exposure | 0.5643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
