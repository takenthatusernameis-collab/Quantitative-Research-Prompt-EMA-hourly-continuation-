# EMA Hourly Continuation — CRV/USDT P89_100

**Symbol:** CRV/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.2494 |
| net_win_rate | 0.3827 |
| gross_profit_factor | 0.6468 |
| gross_win_rate | 0.4244 |
| sharpe_ratio | -9.4781 |
| sortino_ratio | -3.4885 |
| max_drawdown | 0.9893 |
| cagr | -0.8348 |
| net_avg_win | 13.2546 |
| net_avg_loss | -32.9461 |
| avg_hold_time_bars | 1.9707 |
| exposure | 0.0580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
