# EMA Hourly Continuation — CATI/USDT P55_100

**Symbol:** CATI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.4868 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -6.7063 |
| sortino_ratio | -2.5156 |
| max_drawdown | 0.9300 |
| cagr | -0.7145 |
| net_avg_win | 33.6698 |
| net_avg_loss | -54.3758 |
| avg_hold_time_bars | 5.6155 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
