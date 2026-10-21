# EMA Hourly Continuation — RLC/USDT P26_34

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.5857 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8978 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -3.1267 |
| sortino_ratio | -0.7376 |
| max_drawdown | 0.6079 |
| cagr | -0.2889 |
| net_avg_win | 65.5645 |
| net_avg_loss | -94.4327 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
