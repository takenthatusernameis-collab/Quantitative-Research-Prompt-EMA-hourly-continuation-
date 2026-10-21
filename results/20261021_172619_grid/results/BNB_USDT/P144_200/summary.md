# EMA Hourly Continuation — BNB/USDT P144_200

**Symbol:** BNB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.4549 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.8917 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.0542 |
| sortino_ratio | -0.6112 |
| max_drawdown | 0.5083 |
| cagr | -0.2445 |
| net_avg_win | 46.3617 |
| net_avg_loss | -92.7377 |
| avg_hold_time_bars | 6.5707 |
| exposure | 0.0570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
