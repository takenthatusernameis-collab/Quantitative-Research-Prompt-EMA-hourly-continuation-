# EMA Hourly Continuation — KAS/USDT P50_200

**Symbol:** KAS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6963 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.8519 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -1.8319 |
| sortino_ratio | -0.4498 |
| max_drawdown | 0.4278 |
| cagr | -0.1867 |
| net_avg_win | 66.2750 |
| net_avg_loss | -83.8137 |
| avg_hold_time_bars | 23.7893 |
| exposure | 0.3233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
