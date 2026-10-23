# EMA Hourly Continuation — ONE/USDT P26_100

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6922 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 1.0108 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -3.4727 |
| sortino_ratio | -1.2363 |
| max_drawdown | 0.7901 |
| cagr | -0.4459 |
| net_avg_win | 56.4332 |
| net_avg_loss | -76.5592 |
| avg_hold_time_bars | 13.6588 |
| exposure | 0.3949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
