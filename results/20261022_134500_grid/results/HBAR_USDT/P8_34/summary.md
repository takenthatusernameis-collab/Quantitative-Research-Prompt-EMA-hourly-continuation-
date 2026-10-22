# EMA Hourly Continuation — HBAR/USDT P8_34

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1465 |
| net_profit_factor | 0.5601 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 1.0372 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -7.8912 |
| sortino_ratio | -4.2181 |
| max_drawdown | 0.9954 |
| cagr | -0.8795 |
| net_avg_win | 17.7418 |
| net_avg_loss | -30.1177 |
| avg_hold_time_bars | 4.9904 |
| exposure | 0.3323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
