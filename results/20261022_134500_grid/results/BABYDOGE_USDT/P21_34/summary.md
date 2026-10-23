# EMA Hourly Continuation — BABYDOGE/USDT P21_34

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 16 |
| net_profit_factor | 0.7207 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7765 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -0.4093 |
| sortino_ratio | -0.0230 |
| max_drawdown | 0.0630 |
| cagr | -0.0106 |
| net_avg_win | 98.1863 |
| net_avg_loss | -105.9651 |
| avg_hold_time_bars | 13.8125 |
| exposure | 0.0100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
