# EMA Hourly Continuation — T/USDT P144_200

**Symbol:** T/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.4464 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.9357 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -4.4302 |
| sortino_ratio | -1.2031 |
| max_drawdown | 0.7695 |
| cagr | -0.4394 |
| net_avg_win | 37.2859 |
| net_avg_loss | -69.3331 |
| avg_hold_time_bars | 6.1557 |
| exposure | 0.1020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
