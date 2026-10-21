# EMA Hourly Continuation — BSV/USDT P21_55

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.6151 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.4005 |
| sortino_ratio | -1.1260 |
| max_drawdown | 0.7319 |
| cagr | -0.4017 |
| net_avg_win | 45.9562 |
| net_avg_loss | -66.2977 |
| avg_hold_time_bars | 8.2351 |
| exposure | 0.2006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
