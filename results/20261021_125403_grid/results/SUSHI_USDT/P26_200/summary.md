# EMA Hourly Continuation — SUSHI/USDT P26_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7451 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9050 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.5568 |
| sortino_ratio | -0.3869 |
| max_drawdown | 0.3862 |
| cagr | -0.1639 |
| net_avg_win | 72.7605 |
| net_avg_loss | -89.1029 |
| avg_hold_time_bars | 42.4739 |
| exposure | 0.5881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
