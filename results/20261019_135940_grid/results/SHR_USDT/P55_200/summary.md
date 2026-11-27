# EMA Hourly Continuation — SHR/USDT P55_200

**Symbol:** SHR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.5680 |
| net_win_rate | 0.3898 |
| gross_profit_factor | 0.7147 |
| gross_win_rate | 0.3898 |
| sharpe_ratio | -5.1493 |
| sortino_ratio | -1.7785 |
| max_drawdown | 0.8841 |
| cagr | -0.5657 |
| net_avg_win | 48.7026 |
| net_avg_loss | -54.7774 |
| avg_hold_time_bars | 11.7368 |
| exposure | 0.3229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
