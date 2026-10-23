# EMA Hourly Continuation — UQC/USDT P21_100

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.2745 |
| net_win_rate | 0.3041 |
| gross_profit_factor | 0.4807 |
| gross_win_rate | 0.3243 |
| sharpe_ratio | -6.6988 |
| sortino_ratio | -1.6008 |
| max_drawdown | 0.8910 |
| cagr | -0.5848 |
| net_avg_win | 37.4556 |
| net_avg_loss | -59.6179 |
| avg_hold_time_bars | 44.4493 |
| exposure | 0.5955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
