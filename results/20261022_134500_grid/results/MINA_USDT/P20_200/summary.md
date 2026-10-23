# EMA Hourly Continuation — MINA/USDT P20_200

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.7212 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.7838 |
| sortino_ratio | -0.4978 |
| max_drawdown | 0.5128 |
| cagr | -0.2109 |
| net_avg_win | 59.1748 |
| net_avg_loss | -83.3230 |
| avg_hold_time_bars | 36.8175 |
| exposure | 0.6510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
