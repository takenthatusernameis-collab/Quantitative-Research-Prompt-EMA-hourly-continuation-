# EMA Hourly Continuation — AEVO/USDT P55_200

**Symbol:** AEVO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8879 |
| net_win_rate | 0.5199 |
| gross_profit_factor | 1.0754 |
| gross_win_rate | 0.5199 |
| sharpe_ratio | -0.6262 |
| sortino_ratio | -0.1561 |
| max_drawdown | 0.2459 |
| cagr | -0.0721 |
| net_avg_win | 86.8192 |
| net_avg_loss | -105.8725 |
| avg_hold_time_bars | 29.2848 |
| exposure | 0.4002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
