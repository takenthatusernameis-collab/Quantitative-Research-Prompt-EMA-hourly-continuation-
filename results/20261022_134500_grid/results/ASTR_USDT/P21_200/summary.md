# EMA Hourly Continuation — ASTR/USDT P21_200

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7697 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0522 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.5131 |
| sortino_ratio | -0.3860 |
| max_drawdown | 0.4178 |
| cagr | -0.1675 |
| net_avg_win | 75.0175 |
| net_avg_loss | -99.8790 |
| avg_hold_time_bars | 44.8650 |
| exposure | 0.6619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
