# EMA Hourly Continuation — CATI/USDT P21_144

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.6228 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7622 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -2.8399 |
| sortino_ratio | -0.7681 |
| max_drawdown | 0.5515 |
| cagr | -0.3003 |
| net_avg_win | 65.1360 |
| net_avg_loss | -81.3409 |
| avg_hold_time_bars | 32.9638 |
| exposure | 0.5493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
