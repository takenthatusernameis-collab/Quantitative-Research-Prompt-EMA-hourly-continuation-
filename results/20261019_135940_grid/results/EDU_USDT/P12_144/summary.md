# EMA Hourly Continuation — EDU/USDT P12_144

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.7910 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -3.8263 |
| sortino_ratio | -1.2979 |
| max_drawdown | 0.7909 |
| cagr | -0.4623 |
| net_avg_win | 44.4148 |
| net_avg_loss | -59.6372 |
| avg_hold_time_bars | 24.5765 |
| exposure | 0.6539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
