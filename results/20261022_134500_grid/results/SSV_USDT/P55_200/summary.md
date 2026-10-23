# EMA Hourly Continuation — SSV/USDT P55_200

**Symbol:** SSV/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6061 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8485 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -3.3258 |
| sortino_ratio | -0.9678 |
| max_drawdown | 0.6946 |
| cagr | -0.3670 |
| net_avg_win | 53.4523 |
| net_avg_loss | -74.5688 |
| avg_hold_time_bars | 18.6744 |
| exposure | 0.3634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
