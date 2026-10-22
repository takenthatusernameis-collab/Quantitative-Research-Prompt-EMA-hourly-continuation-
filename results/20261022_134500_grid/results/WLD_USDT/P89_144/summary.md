# EMA Hourly Continuation — WLD/USDT P89_144

**Symbol:** WLD/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7163 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0727 |
| gross_win_rate | 0.5179 |
| sharpe_ratio | -2.0784 |
| sortino_ratio | -0.5851 |
| max_drawdown | 0.5553 |
| cagr | -0.2408 |
| net_avg_win | 62.7395 |
| net_avg_loss | -93.1461 |
| avg_hold_time_bars | 6.1026 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
