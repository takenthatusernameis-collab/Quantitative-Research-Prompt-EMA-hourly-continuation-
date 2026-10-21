# EMA Hourly Continuation — DOGS/USDT P8_144

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8225 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.1561 |
| sortino_ratio | -0.3209 |
| max_drawdown | 0.3003 |
| cagr | -0.1388 |
| net_avg_win | 79.6424 |
| net_avg_loss | -95.0425 |
| avg_hold_time_bars | 42.0062 |
| exposure | 0.7198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
