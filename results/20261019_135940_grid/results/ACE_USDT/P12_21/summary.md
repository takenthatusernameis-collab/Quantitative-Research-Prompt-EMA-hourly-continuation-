# EMA Hourly Continuation — ACE/USDT P12_21

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1106 |
| net_profit_factor | 0.4365 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 1.0343 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -8.5661 |
| sortino_ratio | -4.0106 |
| max_drawdown | 0.9937 |
| cagr | -0.8642 |
| net_avg_win | 15.3890 |
| net_avg_loss | -29.0915 |
| avg_hold_time_bars | 3.7523 |
| exposure | 0.1878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
