# EMA Hourly Continuation — FLOKI/USDT P12_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.9037 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0643 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -0.5703 |
| sortino_ratio | -0.1514 |
| max_drawdown | 0.2550 |
| cagr | -0.0707 |
| net_avg_win | 89.6803 |
| net_avg_loss | -105.8507 |
| avg_hold_time_bars | 44.7419 |
| exposure | 0.6935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
