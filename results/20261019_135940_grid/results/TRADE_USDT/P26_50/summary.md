# EMA Hourly Continuation — TRADE/USDT P26_50

**Symbol:** TRADE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.4481 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.7847 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -7.7976 |
| sortino_ratio | -3.0178 |
| max_drawdown | 0.9801 |
| cagr | -0.7877 |
| net_avg_win | 25.5718 |
| net_avg_loss | -38.8376 |
| avg_hold_time_bars | 4.9466 |
| exposure | 0.1727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
