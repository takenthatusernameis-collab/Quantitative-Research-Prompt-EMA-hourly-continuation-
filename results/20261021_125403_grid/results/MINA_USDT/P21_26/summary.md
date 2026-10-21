# EMA Hourly Continuation — MINA/USDT P21_26

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.6933 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0466 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -2.0075 |
| sortino_ratio | -0.4530 |
| max_drawdown | 0.4840 |
| cagr | -0.1884 |
| net_avg_win | 74.3880 |
| net_avg_loss | -108.1604 |
| avg_hold_time_bars | 4.8300 |
| exposure | 0.0542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
