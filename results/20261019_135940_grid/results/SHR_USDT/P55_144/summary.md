# EMA Hourly Continuation — SHR/USDT P55_144

**Symbol:** SHR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.4595 |
| net_win_rate | 0.3451 |
| gross_profit_factor | 0.6106 |
| gross_win_rate | 0.3451 |
| sharpe_ratio | -7.3676 |
| sortino_ratio | -2.7354 |
| max_drawdown | 0.9633 |
| cagr | -0.7285 |
| net_avg_win | 33.5376 |
| net_avg_loss | -38.4672 |
| avg_hold_time_bars | 7.7496 |
| exposure | 0.2479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
