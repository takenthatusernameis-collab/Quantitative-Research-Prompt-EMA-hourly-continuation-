# EMA Hourly Continuation — CPOOL/USDT P12_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.6177 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8279 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -4.6690 |
| sortino_ratio | -1.8480 |
| max_drawdown | 0.8987 |
| cagr | -0.5894 |
| net_avg_win | 40.3048 |
| net_avg_loss | -53.0902 |
| avg_hold_time_bars | 13.7105 |
| exposure | 0.4973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
