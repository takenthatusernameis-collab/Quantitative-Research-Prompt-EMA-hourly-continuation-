# EMA Hourly Continuation — RLC/USDT P12_55

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.7264 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9408 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -2.6635 |
| sortino_ratio | -0.9615 |
| max_drawdown | 0.6889 |
| cagr | -0.3581 |
| net_avg_win | 57.5163 |
| net_avg_loss | -74.6068 |
| avg_hold_time_bars | 12.9124 |
| exposure | 0.3750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
