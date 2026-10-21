# EMA Hourly Continuation — DEEP/USDT P50_144

**Symbol:** DEEP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.9476 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.1027 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -0.2323 |
| sortino_ratio | -0.0580 |
| max_drawdown | 0.1393 |
| cagr | -0.0309 |
| net_avg_win | 87.3703 |
| net_avg_loss | -102.7153 |
| avg_hold_time_bars | 22.3983 |
| exposure | 0.3056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
