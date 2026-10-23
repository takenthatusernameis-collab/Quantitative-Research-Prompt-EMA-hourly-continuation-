# EMA Hourly Continuation — AUCTION/USDT P12_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.5758 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.9178 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -6.8611 |
| sortino_ratio | -2.9237 |
| max_drawdown | 0.9727 |
| cagr | -0.7588 |
| net_avg_win | 32.6734 |
| net_avg_loss | -44.0833 |
| avg_hold_time_bars | 9.6699 |
| exposure | 0.4044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
