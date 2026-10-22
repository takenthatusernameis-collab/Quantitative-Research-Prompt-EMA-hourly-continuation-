# EMA Hourly Continuation — SATS/USDT P100_200

**Symbol:** SATS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.6143 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.7729 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -2.3321 |
| sortino_ratio | -0.5317 |
| max_drawdown | 0.4720 |
| cagr | -0.2167 |
| net_avg_win | 63.7055 |
| net_avg_loss | -82.2501 |
| avg_hold_time_bars | 14.2385 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
