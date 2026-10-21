# EMA Hourly Continuation — ENA/USDT P20_200

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.9190 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -0.3901 |
| sortino_ratio | -0.0967 |
| max_drawdown | 0.2592 |
| cagr | -0.0473 |
| net_avg_win | 85.0258 |
| net_avg_loss | -96.9508 |
| avg_hold_time_bars | 45.7258 |
| exposure | 0.6215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
