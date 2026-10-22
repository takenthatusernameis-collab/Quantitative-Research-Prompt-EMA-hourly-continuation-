# EMA Hourly Continuation — ZIL/USDT P100_144

**Symbol:** ZIL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.7891 |
| net_win_rate | 0.5341 |
| gross_profit_factor | 1.1489 |
| gross_win_rate | 0.5341 |
| sharpe_ratio | -1.1685 |
| sortino_ratio | -0.2664 |
| max_drawdown | 0.2784 |
| cagr | -0.1157 |
| net_avg_win | 74.7318 |
| net_avg_loss | -108.5802 |
| avg_hold_time_bars | 5.7671 |
| exposure | 0.0653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
