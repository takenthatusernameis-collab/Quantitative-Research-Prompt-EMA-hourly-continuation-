# EMA Hourly Continuation — ARB/USDT P89_144

**Symbol:** ARB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.5672 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9860 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -3.7056 |
| sortino_ratio | -1.1325 |
| max_drawdown | 0.7464 |
| cagr | -0.4209 |
| net_avg_win | 41.9848 |
| net_avg_loss | -73.3897 |
| avg_hold_time_bars | 5.0983 |
| exposure | 0.1085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
