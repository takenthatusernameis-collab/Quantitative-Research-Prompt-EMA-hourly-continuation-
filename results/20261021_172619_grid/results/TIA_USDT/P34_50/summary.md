# EMA Hourly Continuation — TIA/USDT P34_50

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.7994 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0476 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.1422 |
| sortino_ratio | -0.2581 |
| max_drawdown | 0.3333 |
| cagr | -0.1118 |
| net_avg_win | 81.4270 |
| net_avg_loss | -106.0704 |
| avg_hold_time_bars | 5.4858 |
| exposure | 0.0616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
