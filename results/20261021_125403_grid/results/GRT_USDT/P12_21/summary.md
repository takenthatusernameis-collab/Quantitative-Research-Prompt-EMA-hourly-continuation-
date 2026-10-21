# EMA Hourly Continuation — GRT/USDT P12_21

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6631 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9363 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.5717 |
| sortino_ratio | -0.6607 |
| max_drawdown | 0.5584 |
| cagr | -0.2612 |
| net_avg_win | 68.7105 |
| net_avg_loss | -93.2581 |
| avg_hold_time_bars | 4.9505 |
| exposure | 0.0724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
