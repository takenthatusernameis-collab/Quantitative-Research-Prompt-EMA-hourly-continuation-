# EMA Hourly Continuation — TWT/USDT P144_200

**Symbol:** TWT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.2976 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.6337 |
| gross_win_rate | 0.4125 |
| sharpe_ratio | -6.4455 |
| sortino_ratio | -1.8469 |
| max_drawdown | 0.9039 |
| cagr | -0.6036 |
| net_avg_win | 23.5892 |
| net_avg_loss | -53.9611 |
| avg_hold_time_bars | 4.1250 |
| exposure | 0.0750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
