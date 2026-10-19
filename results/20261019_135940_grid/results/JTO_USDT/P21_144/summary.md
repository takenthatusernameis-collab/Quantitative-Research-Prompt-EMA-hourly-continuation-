# EMA Hourly Continuation — JTO/USDT P21_144

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.4694 |
| sortino_ratio | -0.7878 |
| max_drawdown | 0.6406 |
| cagr | -0.3088 |
| net_avg_win | 66.6494 |
| net_avg_loss | -84.4307 |
| avg_hold_time_bars | 22.5529 |
| exposure | 0.5228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
