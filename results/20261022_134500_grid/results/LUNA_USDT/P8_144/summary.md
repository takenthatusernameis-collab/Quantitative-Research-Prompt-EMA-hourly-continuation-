# EMA Hourly Continuation — LUNA/USDT P8_144

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.5657 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.9065 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -4.8191 |
| sortino_ratio | -1.6205 |
| max_drawdown | 0.8760 |
| cagr | -0.5594 |
| net_avg_win | 42.3974 |
| net_avg_loss | -62.5717 |
| avg_hold_time_bars | 26.6299 |
| exposure | 0.7130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
