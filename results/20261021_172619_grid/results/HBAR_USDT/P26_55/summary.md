# EMA Hourly Continuation — HBAR/USDT P26_55

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7995 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1136 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -1.4252 |
| sortino_ratio | -0.4011 |
| max_drawdown | 0.4258 |
| cagr | -0.1681 |
| net_avg_win | 73.7722 |
| net_avg_loss | -102.5277 |
| avg_hold_time_bars | 7.0842 |
| exposure | 0.1224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
