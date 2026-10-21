# EMA Hourly Continuation — XTZ/USDT P89_144

**Symbol:** XTZ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7734 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.0854 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -1.2333 |
| sortino_ratio | -0.3007 |
| max_drawdown | 0.3320 |
| cagr | -0.1287 |
| net_avg_win | 66.5515 |
| net_avg_loss | -95.6141 |
| avg_hold_time_bars | 7.7509 |
| exposure | 0.1004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
