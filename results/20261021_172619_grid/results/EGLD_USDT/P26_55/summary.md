# EMA Hourly Continuation — EGLD/USDT P26_55

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6859 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.4511 |
| sortino_ratio | -0.7719 |
| max_drawdown | 0.6189 |
| cagr | -0.2972 |
| net_avg_win | 53.7002 |
| net_avg_loss | -77.3159 |
| avg_hold_time_bars | 7.0541 |
| exposure | 0.1542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
