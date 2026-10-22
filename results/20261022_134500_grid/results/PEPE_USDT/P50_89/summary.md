# EMA Hourly Continuation — PEPE/USDT P50_89

**Symbol:** PEPE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.5093 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.8317 |
| gross_win_rate | 0.4350 |
| sharpe_ratio | -6.7671 |
| sortino_ratio | -2.5480 |
| max_drawdown | 0.9574 |
| cagr | -0.7138 |
| net_avg_win | 32.7778 |
| net_avg_loss | -48.1473 |
| avg_hold_time_bars | 4.1921 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
