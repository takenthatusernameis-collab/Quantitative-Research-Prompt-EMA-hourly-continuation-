# EMA Hourly Continuation — HBAR/USDT P26_34

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 142 |
| net_profit_factor | 0.7830 |
| net_win_rate | 0.5352 |
| gross_profit_factor | 1.1364 |
| gross_win_rate | 0.5352 |
| sharpe_ratio | -0.8663 |
| sortino_ratio | -0.1492 |
| max_drawdown | 0.2161 |
| cagr | -0.0662 |
| net_avg_win | 74.9941 |
| net_avg_loss | -110.2917 |
| avg_hold_time_bars | 4.9789 |
| exposure | 0.0321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
