# EMA Hourly Continuation — CYBER/USDT P8_144

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.9211 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0694 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -0.4214 |
| sortino_ratio | -0.1028 |
| max_drawdown | 0.3148 |
| cagr | -0.0497 |
| net_avg_win | 94.0859 |
| net_avg_loss | -109.4969 |
| avg_hold_time_bars | 61.9062 |
| exposure | 0.8104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
