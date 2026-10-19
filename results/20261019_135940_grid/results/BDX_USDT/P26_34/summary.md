# EMA Hourly Continuation — BDX/USDT P26_34

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1501 |
| net_profit_factor | 0.1028 |
| net_win_rate | 0.1772 |
| gross_profit_factor | 0.4153 |
| gross_win_rate | 0.2658 |
| sharpe_ratio | -25.7330 |
| sortino_ratio | -16.9607 |
| max_drawdown | 1.0000 |
| cagr | -0.9999 |
| net_avg_win | 4.3085 |
| net_avg_loss | -9.0251 |
| avg_hold_time_bars | 1.6356 |
| exposure | 0.1116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
