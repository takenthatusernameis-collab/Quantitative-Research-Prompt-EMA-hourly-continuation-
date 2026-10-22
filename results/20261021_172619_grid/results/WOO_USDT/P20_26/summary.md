# EMA Hourly Continuation — WOO/USDT P20_26

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.5609 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8018 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -3.1887 |
| sortino_ratio | -0.7529 |
| max_drawdown | 0.6202 |
| cagr | -0.2941 |
| net_avg_win | 62.0440 |
| net_avg_loss | -86.1995 |
| avg_hold_time_bars | 4.2080 |
| exposure | 0.0524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
