# EMA Hourly Continuation — EDU/USDT P55_100

**Symbol:** EDU/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.4763 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.7459 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -5.6544 |
| sortino_ratio | -2.0523 |
| max_drawdown | 0.9195 |
| cagr | -0.6264 |
| net_avg_win | 28.9462 |
| net_avg_loss | -47.0488 |
| avg_hold_time_bars | 5.4727 |
| exposure | 0.1634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
