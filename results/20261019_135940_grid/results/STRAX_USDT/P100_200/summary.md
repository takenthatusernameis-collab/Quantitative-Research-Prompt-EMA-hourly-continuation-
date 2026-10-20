# EMA Hourly Continuation — STRAX/USDT P100_200

**Symbol:** STRAX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.4163 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.6600 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -5.8599 |
| sortino_ratio | -1.8101 |
| max_drawdown | 0.8835 |
| cagr | -0.5742 |
| net_avg_win | 34.3457 |
| net_avg_loss | -52.4254 |
| avg_hold_time_bars | 9.1338 |
| exposure | 0.1967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
