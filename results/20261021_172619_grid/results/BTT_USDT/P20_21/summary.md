# EMA Hourly Continuation — BTT/USDT P20_21

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 0.3109 |
| net_win_rate | 0.3611 |
| gross_profit_factor | 0.6231 |
| gross_win_rate | 0.3611 |
| sharpe_ratio | -4.4732 |
| sortino_ratio | -0.7916 |
| max_drawdown | 0.6201 |
| cagr | -0.3154 |
| net_avg_win | 53.2679 |
| net_avg_loss | -96.8397 |
| avg_hold_time_bars | 5.7639 |
| exposure | 0.0377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
