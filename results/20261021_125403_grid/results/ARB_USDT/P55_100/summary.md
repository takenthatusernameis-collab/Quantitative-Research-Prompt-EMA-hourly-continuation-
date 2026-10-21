# EMA Hourly Continuation — ARB/USDT P55_100

**Symbol:** ARB/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8151 |
| net_win_rate | 0.5199 |
| gross_profit_factor | 1.0687 |
| gross_win_rate | 0.5199 |
| sharpe_ratio | -1.0760 |
| sortino_ratio | -0.2804 |
| max_drawdown | 0.3768 |
| cagr | -0.1216 |
| net_avg_win | 72.0755 |
| net_avg_loss | -95.7494 |
| avg_hold_time_bars | 8.2661 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
