# EMA Hourly Continuation — CRO/USDT P21_50

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1035 |
| net_profit_factor | 0.3395 |
| net_win_rate | 0.4029 |
| gross_profit_factor | 0.8139 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -10.5233 |
| sortino_ratio | -4.7941 |
| max_drawdown | 0.9980 |
| cagr | -0.9144 |
| net_avg_win | 12.3022 |
| net_avg_loss | -24.4485 |
| avg_hold_time_bars | 4.6348 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
