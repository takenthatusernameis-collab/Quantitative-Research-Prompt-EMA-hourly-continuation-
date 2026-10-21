# EMA Hourly Continuation — HNT/USDT P12_55

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.6967 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -2.5708 |
| sortino_ratio | -0.8928 |
| max_drawdown | 0.6502 |
| cagr | -0.3366 |
| net_avg_win | 52.5764 |
| net_avg_loss | -67.3197 |
| avg_hold_time_bars | 12.7332 |
| exposure | 0.3450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
