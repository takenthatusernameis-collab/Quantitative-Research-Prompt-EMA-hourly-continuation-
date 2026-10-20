# EMA Hourly Continuation — RIO/USDT P12_144

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6680 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8776 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -3.6351 |
| sortino_ratio | -1.3132 |
| max_drawdown | 0.8054 |
| cagr | -0.4688 |
| net_avg_win | 52.8011 |
| net_avg_loss | -66.6813 |
| avg_hold_time_bars | 20.5379 |
| exposure | 0.6223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
