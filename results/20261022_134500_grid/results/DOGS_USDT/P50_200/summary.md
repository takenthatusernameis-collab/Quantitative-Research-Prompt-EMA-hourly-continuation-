# EMA Hourly Continuation — DOGS/USDT P50_200

**Symbol:** DOGS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6668 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.6503 |
| sortino_ratio | -0.7376 |
| max_drawdown | 0.5688 |
| cagr | -0.2986 |
| net_avg_win | 65.5390 |
| net_avg_loss | -91.5513 |
| avg_hold_time_bars | 21.3609 |
| exposure | 0.3830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
