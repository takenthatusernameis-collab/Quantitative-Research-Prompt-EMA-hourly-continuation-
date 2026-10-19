# EMA Hourly Continuation — OP/USDT P8_89

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -4.1073 |
| sortino_ratio | -1.5149 |
| max_drawdown | 0.8490 |
| cagr | -0.5137 |
| net_avg_win | 41.7067 |
| net_avg_loss | -58.6105 |
| avg_hold_time_bars | 20.4978 |
| exposure | 0.6401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
