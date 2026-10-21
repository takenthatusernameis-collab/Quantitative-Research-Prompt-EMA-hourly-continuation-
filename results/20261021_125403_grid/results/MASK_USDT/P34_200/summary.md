# EMA Hourly Continuation — MASK/USDT P34_200

**Symbol:** MASK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.0833 |
| sortino_ratio | -0.5462 |
| max_drawdown | 0.4704 |
| cagr | -0.2221 |
| net_avg_win | 59.6940 |
| net_avg_loss | -80.7268 |
| avg_hold_time_bars | 32.7485 |
| exposure | 0.5031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
