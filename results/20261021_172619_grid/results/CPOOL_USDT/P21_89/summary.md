# EMA Hourly Continuation — CPOOL/USDT P21_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8897 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0456 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -0.7749 |
| sortino_ratio | -0.2493 |
| max_drawdown | 0.3157 |
| cagr | -0.1130 |
| net_avg_win | 81.2969 |
| net_avg_loss | -96.6163 |
| avg_hold_time_bars | 13.3705 |
| exposure | 0.3051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
