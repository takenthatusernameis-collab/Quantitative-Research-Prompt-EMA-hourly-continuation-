# EMA Hourly Continuation — SAND/USDT P144_200

**Symbol:** SAND/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.4515 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -4.8865 |
| sortino_ratio | -1.3670 |
| max_drawdown | 0.8292 |
| cagr | -0.5031 |
| net_avg_win | 37.2068 |
| net_avg_loss | -70.1487 |
| avg_hold_time_bars | 4.3090 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
