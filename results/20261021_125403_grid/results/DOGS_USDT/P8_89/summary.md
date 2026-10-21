# EMA Hourly Continuation — DOGS/USDT P8_89

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.9430 |
| net_win_rate | 0.5342 |
| gross_profit_factor | 1.1337 |
| gross_win_rate | 0.5342 |
| sharpe_ratio | -0.3505 |
| sortino_ratio | -0.1164 |
| max_drawdown | 0.1585 |
| cagr | -0.0594 |
| net_avg_win | 84.3709 |
| net_avg_loss | -102.6198 |
| avg_hold_time_bars | 24.2274 |
| exposure | 0.5822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
