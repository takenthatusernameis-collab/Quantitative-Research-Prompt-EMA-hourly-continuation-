# EMA Hourly Continuation — TRX/USDT P34_200

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.5617 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -3.0848 |
| sortino_ratio | -0.7590 |
| max_drawdown | 0.5936 |
| cagr | -0.2988 |
| net_avg_win | 51.7767 |
| net_avg_loss | -89.1305 |
| avg_hold_time_bars | 29.4579 |
| exposure | 0.3977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
