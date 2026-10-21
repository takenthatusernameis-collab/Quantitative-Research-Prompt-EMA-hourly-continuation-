# EMA Hourly Continuation — ROSE/USDT P26_89

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.8274 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0221 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -1.4161 |
| sortino_ratio | -0.4490 |
| max_drawdown | 0.4733 |
| cagr | -0.1883 |
| net_avg_win | 79.1330 |
| net_avg_loss | -97.2161 |
| avg_hold_time_bars | 13.8000 |
| exposure | 0.3074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
