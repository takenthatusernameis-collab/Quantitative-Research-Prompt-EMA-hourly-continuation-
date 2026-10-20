# EMA Hourly Continuation — API3/USDT P34_100

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6608 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9745 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -3.6890 |
| sortino_ratio | -1.3463 |
| max_drawdown | 0.8047 |
| cagr | -0.4678 |
| net_avg_win | 49.0099 |
| net_avg_loss | -67.5370 |
| avg_hold_time_bars | 9.9321 |
| exposure | 0.2993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
