# EMA Hourly Continuation — AURORA/USDT P20_200

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.5516 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.8174 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -3.9447 |
| sortino_ratio | -1.1029 |
| max_drawdown | 0.7558 |
| cagr | -0.4167 |
| net_avg_win | 52.4463 |
| net_avg_loss | -72.5582 |
| avg_hold_time_bars | 31.6244 |
| exposure | 0.5779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
