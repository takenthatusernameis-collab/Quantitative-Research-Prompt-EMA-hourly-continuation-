# EMA Hourly Continuation — CWEB/USDT P20_200

**Symbol:** CWEB/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7682 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0736 |
| gross_win_rate | 0.5153 |
| sharpe_ratio | -1.4316 |
| sortino_ratio | -0.3289 |
| max_drawdown | 0.4101 |
| cagr | -0.1458 |
| net_avg_win | 80.8388 |
| net_avg_loss | -110.1620 |
| avg_hold_time_bars | 59.4313 |
| exposure | 0.7078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
