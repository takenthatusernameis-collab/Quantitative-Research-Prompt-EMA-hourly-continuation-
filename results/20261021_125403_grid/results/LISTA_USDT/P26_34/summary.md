# EMA Hourly Continuation — LISTA/USDT P26_34

**Symbol:** LISTA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.6509 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.6297 |
| sortino_ratio | -0.6649 |
| max_drawdown | 0.5354 |
| cagr | -0.2645 |
| net_avg_win | 69.1780 |
| net_avg_loss | -94.6186 |
| avg_hold_time_bars | 6.1229 |
| exposure | 0.0877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
