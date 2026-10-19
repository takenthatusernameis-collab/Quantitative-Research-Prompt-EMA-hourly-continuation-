# EMA Hourly Continuation — OP/USDT P26_144

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.5709 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.7993 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -3.6688 |
| sortino_ratio | -1.0967 |
| max_drawdown | 0.7305 |
| cagr | -0.4041 |
| net_avg_win | 48.1648 |
| net_avg_loss | -67.8253 |
| avg_hold_time_bars | 25.2461 |
| exposure | 0.5175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
