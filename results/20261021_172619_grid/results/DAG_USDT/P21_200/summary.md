# EMA Hourly Continuation — DAG/USDT P21_200

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.8449 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -0.8588 |
| sortino_ratio | -0.2186 |
| max_drawdown | 0.3012 |
| cagr | -0.0976 |
| net_avg_win | 78.9376 |
| net_avg_loss | -91.6715 |
| avg_hold_time_bars | 38.5268 |
| exposure | 0.5551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
