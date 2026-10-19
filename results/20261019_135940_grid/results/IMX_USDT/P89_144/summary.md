# EMA Hourly Continuation — IMX/USDT P89_144

**Symbol:** IMX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5421 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9123 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -4.0159 |
| sortino_ratio | -1.2707 |
| max_drawdown | 0.7951 |
| cagr | -0.4582 |
| net_avg_win | 38.3420 |
| net_avg_loss | -65.1003 |
| avg_hold_time_bars | 5.0079 |
| exposure | 0.1149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
