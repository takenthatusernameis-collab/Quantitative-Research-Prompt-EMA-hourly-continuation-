# EMA Hourly Continuation — CPOOL/USDT P20_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.7367 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9727 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.6683 |
| sortino_ratio | -0.9468 |
| max_drawdown | 0.7094 |
| cagr | -0.3654 |
| net_avg_win | 60.8542 |
| net_avg_loss | -79.3109 |
| avg_hold_time_bars | 15.6980 |
| exposure | 0.4560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
