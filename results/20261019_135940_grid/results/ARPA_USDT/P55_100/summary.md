# EMA Hourly Continuation — ARPA/USDT P55_100

**Symbol:** ARPA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.4424 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7913 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -6.9439 |
| sortino_ratio | -2.5837 |
| max_drawdown | 0.9597 |
| cagr | -0.7162 |
| net_avg_win | 25.7704 |
| net_avg_loss | -42.7493 |
| avg_hold_time_bars | 5.4821 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
