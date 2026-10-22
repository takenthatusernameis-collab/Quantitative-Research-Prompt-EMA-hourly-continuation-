# EMA Hourly Continuation — EGLD/USDT P26_55

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.4129 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8244 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -7.7962 |
| sortino_ratio | -3.3573 |
| max_drawdown | 0.9849 |
| cagr | -0.8104 |
| net_avg_win | 16.7260 |
| net_avg_loss | -32.4388 |
| avg_hold_time_bars | 4.5091 |
| exposure | 0.1908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
