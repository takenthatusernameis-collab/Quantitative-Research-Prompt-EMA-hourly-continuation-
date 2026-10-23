# EMA Hourly Continuation — PEOPLE/USDT P8_12

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1752 |
| net_profit_factor | 0.2316 |
| net_win_rate | 0.3853 |
| gross_profit_factor | 0.5591 |
| gross_win_rate | 0.4161 |
| sharpe_ratio | -15.4703 |
| sortino_ratio | -9.2300 |
| max_drawdown | 1.0000 |
| cagr | -0.9916 |
| net_avg_win | 4.4662 |
| net_avg_loss | -12.0841 |
| avg_hold_time_bars | 2.1210 |
| exposure | 0.1682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
