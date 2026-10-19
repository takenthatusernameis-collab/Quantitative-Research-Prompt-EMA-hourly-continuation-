# EMA Hourly Continuation — PYTH/USDT P20_89

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.5820 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -4.5975 |
| sortino_ratio | -1.7385 |
| max_drawdown | 0.8815 |
| cagr | -0.5651 |
| net_avg_win | 36.7574 |
| net_avg_loss | -53.2186 |
| avg_hold_time_bars | 11.3209 |
| exposure | 0.3736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
