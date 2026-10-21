# EMA Hourly Continuation — SUI/USDT P34_100

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.9584 |
| net_win_rate | 0.5492 |
| gross_profit_factor | 1.2064 |
| gross_win_rate | 0.5492 |
| sharpe_ratio | -0.2197 |
| sortino_ratio | -0.0626 |
| max_drawdown | 0.2270 |
| cagr | -0.0344 |
| net_avg_win | 91.2501 |
| net_avg_loss | -116.0095 |
| avg_hold_time_bars | 12.5285 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
