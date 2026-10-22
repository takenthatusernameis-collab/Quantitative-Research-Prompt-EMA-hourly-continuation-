# EMA Hourly Continuation — LINK/USDT P34_89

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5629 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -5.2630 |
| sortino_ratio | -1.8445 |
| max_drawdown | 0.9016 |
| cagr | -0.5985 |
| net_avg_win | 39.6469 |
| net_avg_loss | -61.0258 |
| avg_hold_time_bars | 8.1781 |
| exposure | 0.2338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
