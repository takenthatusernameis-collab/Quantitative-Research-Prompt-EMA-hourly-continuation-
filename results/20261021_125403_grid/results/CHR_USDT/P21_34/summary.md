# EMA Hourly Continuation — CHR/USDT P21_34

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6232 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -3.1950 |
| sortino_ratio | -0.9182 |
| max_drawdown | 0.6586 |
| cagr | -0.3432 |
| net_avg_win | 58.1395 |
| net_avg_loss | -78.5117 |
| avg_hold_time_bars | 5.8993 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
