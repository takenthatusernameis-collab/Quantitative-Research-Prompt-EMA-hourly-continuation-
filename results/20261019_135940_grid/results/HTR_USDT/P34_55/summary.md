# EMA Hourly Continuation — HTR/USDT P34_55

**Symbol:** HTR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.4404 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.8041 |
| gross_win_rate | 0.4103 |
| sharpe_ratio | -8.9901 |
| sortino_ratio | -3.7117 |
| max_drawdown | 0.9920 |
| cagr | -0.8506 |
| net_avg_win | 22.8130 |
| net_avg_loss | -34.3364 |
| avg_hold_time_bars | 3.8380 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
