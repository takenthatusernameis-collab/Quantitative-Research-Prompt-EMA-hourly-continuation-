# EMA Hourly Continuation — ONDO/USDT P20_55

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.5708 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.9259 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -5.8632 |
| sortino_ratio | -2.5338 |
| max_drawdown | 0.9562 |
| cagr | -0.7084 |
| net_avg_win | 28.5917 |
| net_avg_loss | -44.2183 |
| avg_hold_time_bars | 5.0275 |
| exposure | 0.2164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
