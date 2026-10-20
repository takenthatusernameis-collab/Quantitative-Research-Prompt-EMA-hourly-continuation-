# EMA Hourly Continuation — VELO/USDT P34_50

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.4344 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.7435 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -8.3082 |
| sortino_ratio | -3.5931 |
| max_drawdown | 0.9889 |
| cagr | -0.8295 |
| net_avg_win | 19.2147 |
| net_avg_loss | -32.4761 |
| avg_hold_time_bars | 2.7738 |
| exposure | 0.1176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
