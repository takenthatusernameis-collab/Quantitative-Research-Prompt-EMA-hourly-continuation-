# EMA Hourly Continuation — GMEE/USDT P55_200

**Symbol:** GMEE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.4761 |
| net_win_rate | 0.4027 |
| gross_profit_factor | 0.6596 |
| gross_win_rate | 0.4082 |
| sharpe_ratio | -4.1048 |
| sortino_ratio | -1.0993 |
| max_drawdown | 0.7512 |
| cagr | -0.4057 |
| net_avg_win | 45.0895 |
| net_avg_loss | -63.8600 |
| avg_hold_time_bars | 21.5342 |
| exposure | 0.3573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
