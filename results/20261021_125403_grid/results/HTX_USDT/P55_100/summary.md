# EMA Hourly Continuation — HTX/USDT P55_100

**Symbol:** HTX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.3741 |
| net_win_rate | 0.3478 |
| gross_profit_factor | 0.6472 |
| gross_win_rate | 0.3505 |
| sharpe_ratio | -6.9525 |
| sortino_ratio | -1.9400 |
| max_drawdown | 0.9058 |
| cagr | -0.6062 |
| net_avg_win | 42.2513 |
| net_avg_loss | -60.2291 |
| avg_hold_time_bars | 9.6658 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
