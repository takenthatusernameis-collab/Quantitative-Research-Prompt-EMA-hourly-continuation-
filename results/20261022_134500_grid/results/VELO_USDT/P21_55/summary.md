# EMA Hourly Continuation — VELO/USDT P21_55

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.5646 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -5.8851 |
| sortino_ratio | -2.6255 |
| max_drawdown | 0.9600 |
| cagr | -0.7165 |
| net_avg_win | 26.8847 |
| net_avg_loss | -40.2912 |
| avg_hold_time_bars | 4.9167 |
| exposure | 0.2253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
