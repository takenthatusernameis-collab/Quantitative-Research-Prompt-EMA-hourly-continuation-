# EMA Hourly Continuation — CTSI/USDT P34_50

**Symbol:** CTSI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.4262 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -8.7164 |
| sortino_ratio | -3.8045 |
| max_drawdown | 0.9913 |
| cagr | -0.8456 |
| net_avg_win | 18.3071 |
| net_avg_loss | -32.2159 |
| avg_hold_time_bars | 3.3753 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
