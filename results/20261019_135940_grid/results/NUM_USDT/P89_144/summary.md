# EMA Hourly Continuation — NUM/USDT P89_144

**Symbol:** NUM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.4728 |
| net_win_rate | 0.3851 |
| gross_profit_factor | 0.7603 |
| gross_win_rate | 0.3952 |
| sharpe_ratio | -5.8833 |
| sortino_ratio | -1.8592 |
| max_drawdown | 0.8967 |
| cagr | -0.5850 |
| net_avg_win | 41.7927 |
| net_avg_loss | -55.3564 |
| avg_hold_time_bars | 7.2319 |
| exposure | 0.1630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
