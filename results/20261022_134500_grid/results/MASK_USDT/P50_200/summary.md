# EMA Hourly Continuation — MASK/USDT P50_200

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6380 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 1.0176 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -2.7920 |
| sortino_ratio | -0.8068 |
| max_drawdown | 0.6306 |
| cagr | -0.3204 |
| net_avg_win | 52.8632 |
| net_avg_loss | -80.1465 |
| avg_hold_time_bars | 21.4204 |
| exposure | 0.4099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
