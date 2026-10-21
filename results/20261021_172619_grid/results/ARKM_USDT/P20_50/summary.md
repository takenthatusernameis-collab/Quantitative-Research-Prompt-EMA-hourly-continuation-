# EMA Hourly Continuation — ARKM/USDT P20_50

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7181 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -2.6358 |
| sortino_ratio | -0.8479 |
| max_drawdown | 0.6564 |
| cagr | -0.3229 |
| net_avg_win | 66.5375 |
| net_avg_loss | -81.7214 |
| avg_hold_time_bars | 7.5667 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
