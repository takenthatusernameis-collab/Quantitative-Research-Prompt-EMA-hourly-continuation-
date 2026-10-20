# EMA Hourly Continuation — 1INCH/USDT P50_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5143 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -5.0422 |
| sortino_ratio | -1.6235 |
| max_drawdown | 0.8772 |
| cagr | -0.5585 |
| net_avg_win | 38.4560 |
| net_avg_loss | -61.2489 |
| avg_hold_time_bars | 12.4728 |
| exposure | 0.3022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
