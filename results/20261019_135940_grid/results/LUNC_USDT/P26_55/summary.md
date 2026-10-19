# EMA Hourly Continuation — LUNC/USDT P26_55

**Symbol:** LUNC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1002 |
| net_profit_factor | 0.3326 |
| net_win_rate | 0.4142 |
| gross_profit_factor | 0.7240 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -9.5603 |
| sortino_ratio | -4.3016 |
| max_drawdown | 0.9954 |
| cagr | -0.8810 |
| net_avg_win | 11.9514 |
| net_avg_loss | -25.4040 |
| avg_hold_time_bars | 3.7405 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
