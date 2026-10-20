# EMA Hourly Continuation — DEEP/USDT P144_200

**Symbol:** DEEP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.5775 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8859 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -3.3181 |
| sortino_ratio | -0.8758 |
| max_drawdown | 0.5920 |
| cagr | -0.3485 |
| net_avg_win | 59.9114 |
| net_avg_loss | -90.0890 |
| avg_hold_time_bars | 4.8486 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
