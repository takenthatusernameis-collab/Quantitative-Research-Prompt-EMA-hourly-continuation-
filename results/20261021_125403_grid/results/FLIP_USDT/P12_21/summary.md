# EMA Hourly Continuation — FLIP/USDT P12_21

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.4642 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.8387 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -6.1176 |
| sortino_ratio | -1.9433 |
| max_drawdown | 0.9104 |
| cagr | -0.6154 |
| net_avg_win | 36.8036 |
| net_avg_loss | -59.3308 |
| avg_hold_time_bars | 8.0080 |
| exposure | 0.1820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
