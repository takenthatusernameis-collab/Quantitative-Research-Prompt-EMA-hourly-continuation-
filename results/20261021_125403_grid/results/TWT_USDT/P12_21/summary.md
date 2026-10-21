# EMA Hourly Continuation — TWT/USDT P12_21

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6619 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0878 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -2.6032 |
| sortino_ratio | -0.7606 |
| max_drawdown | 0.5881 |
| cagr | -0.2928 |
| net_avg_win | 53.4065 |
| net_avg_loss | -87.6839 |
| avg_hold_time_bars | 4.3325 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
