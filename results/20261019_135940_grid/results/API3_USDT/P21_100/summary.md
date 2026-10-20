# EMA Hourly Continuation — API3/USDT P21_100

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.6317 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9196 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -3.8201 |
| sortino_ratio | -1.4121 |
| max_drawdown | 0.8217 |
| cagr | -0.4849 |
| net_avg_win | 43.3407 |
| net_avg_loss | -61.0032 |
| avg_hold_time_bars | 13.1818 |
| exposure | 0.4086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
