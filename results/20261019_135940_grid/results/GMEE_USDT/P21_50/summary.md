# EMA Hourly Continuation — GMEE/USDT P21_50

**Symbol:** GMEE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 989 |
| net_profit_factor | 0.4802 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.7559 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -7.7026 |
| sortino_ratio | -3.4091 |
| max_drawdown | 0.9850 |
| cagr | -0.8115 |
| net_avg_win | 21.6603 |
| net_avg_loss | -33.2970 |
| avg_hold_time_bars | 4.9373 |
| exposure | 0.2220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
