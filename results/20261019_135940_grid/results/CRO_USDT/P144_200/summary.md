# EMA Hourly Continuation — CRO/USDT P144_200

**Symbol:** CRO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.3063 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.7336 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -6.2094 |
| sortino_ratio | -1.8184 |
| max_drawdown | 0.9066 |
| cagr | -0.6054 |
| net_avg_win | 21.7881 |
| net_avg_loss | -54.0209 |
| avg_hold_time_bars | 4.2406 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
