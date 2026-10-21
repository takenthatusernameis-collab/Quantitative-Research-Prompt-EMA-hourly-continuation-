# EMA Hourly Continuation — CHZ/USDT P20_200

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.9794 |
| net_win_rate | 0.5461 |
| gross_profit_factor | 1.1864 |
| gross_win_rate | 0.5461 |
| sharpe_ratio | -0.0639 |
| sortino_ratio | -0.0155 |
| max_drawdown | 0.2770 |
| cagr | -0.0124 |
| net_avg_win | 95.0974 |
| net_avg_loss | -116.8148 |
| avg_hold_time_bars | 50.9858 |
| exposure | 0.6535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
