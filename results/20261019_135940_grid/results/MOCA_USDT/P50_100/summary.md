# EMA Hourly Continuation — MOCA/USDT P50_100

**Symbol:** MOCA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.5115 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -5.4781 |
| sortino_ratio | -1.8944 |
| max_drawdown | 0.8888 |
| cagr | -0.6069 |
| net_avg_win | 37.6331 |
| net_avg_loss | -59.1041 |
| avg_hold_time_bars | 6.2036 |
| exposure | 0.1710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
