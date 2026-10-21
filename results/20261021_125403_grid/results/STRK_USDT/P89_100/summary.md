# EMA Hourly Continuation — STRK/USDT P89_100

**Symbol:** STRK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 91 |
| net_profit_factor | 0.6092 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8060 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -1.4155 |
| sortino_ratio | -0.1921 |
| max_drawdown | 0.2030 |
| cagr | -0.0844 |
| net_avg_win | 75.5147 |
| net_avg_loss | -101.6518 |
| avg_hold_time_bars | 4.5714 |
| exposure | 0.0189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
