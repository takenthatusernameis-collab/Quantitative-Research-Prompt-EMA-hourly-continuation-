# EMA Hourly Continuation — JTO/USDT P8_50

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.6138 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4546 |
| sharpe_ratio | -5.8883 |
| sortino_ratio | -2.7035 |
| max_drawdown | 0.9648 |
| cagr | -0.7271 |
| net_avg_win | 31.7742 |
| net_avg_loss | -42.3469 |
| avg_hold_time_bars | 9.9654 |
| exposure | 0.4842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
