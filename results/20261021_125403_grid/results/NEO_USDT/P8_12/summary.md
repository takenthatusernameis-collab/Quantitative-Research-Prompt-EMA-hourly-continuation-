# EMA Hourly Continuation — NEO/USDT P8_12

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1439 |
| gross_win_rate | 0.5298 |
| sharpe_ratio | -1.8481 |
| sortino_ratio | -0.4509 |
| max_drawdown | 0.4239 |
| cagr | -0.1860 |
| net_avg_win | 68.0004 |
| net_avg_loss | -106.7427 |
| avg_hold_time_bars | 4.6842 |
| exposure | 0.0607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
