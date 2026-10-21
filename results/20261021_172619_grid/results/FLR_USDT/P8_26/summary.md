# EMA Hourly Continuation — FLR/USDT P8_26

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8297 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -4.2730 |
| sortino_ratio | -1.5653 |
| max_drawdown | 0.8405 |
| cagr | -0.5124 |
| net_avg_win | 39.4948 |
| net_avg_loss | -57.4014 |
| avg_hold_time_bars | 6.1994 |
| exposure | 0.1851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
