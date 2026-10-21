# EMA Hourly Continuation — BAT/USDT P26_34

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.5383 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9014 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -3.5140 |
| sortino_ratio | -0.9115 |
| max_drawdown | 0.6682 |
| cagr | -0.3432 |
| net_avg_win | 50.0273 |
| net_avg_loss | -81.6472 |
| avg_hold_time_bars | 4.7046 |
| exposure | 0.0695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
