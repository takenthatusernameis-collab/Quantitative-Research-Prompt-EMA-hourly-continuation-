# EMA Hourly Continuation — RIO/USDT P21_200

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6537 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8455 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -3.1974 |
| sortino_ratio | -1.0059 |
| max_drawdown | 0.7254 |
| cagr | -0.3796 |
| net_avg_win | 58.8246 |
| net_avg_loss | -73.5019 |
| avg_hold_time_bars | 26.5323 |
| exposure | 0.6042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
