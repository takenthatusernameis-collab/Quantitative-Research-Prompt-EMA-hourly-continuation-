# EMA Hourly Continuation — ASTR/USDT P20_21

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1110 |
| net_profit_factor | 0.1188 |
| net_win_rate | 0.3054 |
| gross_profit_factor | 0.6017 |
| gross_win_rate | 0.4117 |
| sharpe_ratio | -16.7599 |
| sortino_ratio | -8.4980 |
| max_drawdown | 1.0000 |
| cagr | -0.9914 |
| net_avg_win | 3.9750 |
| net_avg_loss | -14.7179 |
| avg_hold_time_bars | 2.3225 |
| exposure | 0.1167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
