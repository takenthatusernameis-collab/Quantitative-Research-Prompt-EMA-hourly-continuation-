# EMA Hourly Continuation — FLOW/USDT P50_55

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 137 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0710 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.3208 |
| sortino_ratio | -0.2227 |
| max_drawdown | 0.2722 |
| cagr | -0.0969 |
| net_avg_win | 80.9251 |
| net_avg_loss | -115.3197 |
| avg_hold_time_bars | 4.1022 |
| exposure | 0.0255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
