# EMA Hourly Continuation — MTL/USDT P100_144

**Symbol:** MTL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.3840 |
| net_win_rate | 0.4208 |
| gross_profit_factor | 0.7831 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -6.1534 |
| sortino_ratio | -1.8672 |
| max_drawdown | 0.9065 |
| cagr | -0.6091 |
| net_avg_win | 29.1249 |
| net_avg_loss | -55.1128 |
| avg_hold_time_bars | 6.6074 |
| exposure | 0.1378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
