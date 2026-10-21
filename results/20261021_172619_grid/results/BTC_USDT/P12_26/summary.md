# EMA Hourly Continuation — BTC/USDT P12_26

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.4727 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9396 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -4.4875 |
| sortino_ratio | -1.2895 |
| max_drawdown | 0.8181 |
| cagr | -0.4496 |
| net_avg_win | 33.9470 |
| net_avg_loss | -66.8677 |
| avg_hold_time_bars | 6.9464 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
