# EMA Hourly Continuation — SATS/USDT P20_200

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5820 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8194 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -3.2997 |
| sortino_ratio | -0.9327 |
| max_drawdown | 0.6908 |
| cagr | -0.3575 |
| net_avg_win | 52.0139 |
| net_avg_loss | -70.5526 |
| avg_hold_time_bars | 32.1814 |
| exposure | 0.5941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
