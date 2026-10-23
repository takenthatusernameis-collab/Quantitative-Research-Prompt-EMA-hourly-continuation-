# EMA Hourly Continuation — VELO/USDT P21_34

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1186 |
| net_profit_factor | 0.4460 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.7644 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -10.0322 |
| sortino_ratio | -4.8899 |
| max_drawdown | 0.9978 |
| cagr | -0.9119 |
| net_avg_win | 16.4600 |
| net_avg_loss | -25.8024 |
| avg_hold_time_bars | 2.5194 |
| exposure | 0.1358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
