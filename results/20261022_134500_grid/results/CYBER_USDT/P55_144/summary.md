# EMA Hourly Continuation — CYBER/USDT P55_144

**Symbol:** CYBER/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6608 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -2.6022 |
| sortino_ratio | -0.8160 |
| max_drawdown | 0.6411 |
| cagr | -0.3167 |
| net_avg_win | 49.5658 |
| net_avg_loss | -74.0882 |
| avg_hold_time_bars | 12.1910 |
| exposure | 0.2699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
