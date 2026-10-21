# EMA Hourly Continuation — RUNE/USDT P21_34

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.7174 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0533 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.9798 |
| sortino_ratio | -0.4949 |
| max_drawdown | 0.4691 |
| cagr | -0.2029 |
| net_avg_win | 72.0611 |
| net_avg_loss | -103.1399 |
| avg_hold_time_bars | 4.6457 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
