# EMA Hourly Continuation — GMT/USDT P100_144

**Symbol:** GMT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.7031 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.7575 |
| sortino_ratio | -0.3883 |
| max_drawdown | 0.4211 |
| cagr | -0.1630 |
| net_avg_win | 73.5695 |
| net_avg_loss | -99.4840 |
| avg_hold_time_bars | 6.1471 |
| exposure | 0.0665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
