# EMA Hourly Continuation — LSK/USDT P12_26

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1106 |
| net_profit_factor | 0.4614 |
| net_win_rate | 0.4268 |
| gross_profit_factor | 0.9656 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -9.0985 |
| sortino_ratio | -4.3009 |
| max_drawdown | 0.9951 |
| cagr | -0.8778 |
| net_avg_win | 18.0570 |
| net_avg_loss | -29.1355 |
| avg_hold_time_bars | 4.3065 |
| exposure | 0.2165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
