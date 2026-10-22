# EMA Hourly Continuation — LQTY/USDT P20_26

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6886 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0300 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.0679 |
| sortino_ratio | -0.5116 |
| max_drawdown | 0.4702 |
| cagr | -0.2079 |
| net_avg_win | 65.5199 |
| net_avg_loss | -97.0960 |
| avg_hold_time_bars | 4.7475 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
