# EMA Hourly Continuation — ONE/USDT P34_200

**Symbol:** ONE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8502 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0023 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -0.9198 |
| sortino_ratio | -0.2306 |
| max_drawdown | 0.3146 |
| cagr | -0.1025 |
| net_avg_win | 88.2181 |
| net_avg_loss | -103.0936 |
| avg_hold_time_bars | 36.3941 |
| exposure | 0.5079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
