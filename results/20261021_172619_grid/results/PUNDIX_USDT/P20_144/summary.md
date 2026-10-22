# EMA Hourly Continuation — PUNDIX/USDT P20_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7524 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.8035 |
| sortino_ratio | -0.5268 |
| max_drawdown | 0.4715 |
| cagr | -0.2165 |
| net_avg_win | 67.2482 |
| net_avg_loss | -87.6845 |
| avg_hold_time_bars | 29.7488 |
| exposure | 0.5652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
