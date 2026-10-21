# EMA Hourly Continuation — RIO/USDT P21_34

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6603 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.7942 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -2.2349 |
| sortino_ratio | -0.5193 |
| max_drawdown | 0.4534 |
| cagr | -0.2129 |
| net_avg_win | 74.5094 |
| net_avg_loss | -88.0175 |
| avg_hold_time_bars | 6.3633 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
