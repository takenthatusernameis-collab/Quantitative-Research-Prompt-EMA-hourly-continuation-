# EMA Hourly Continuation — SUI/USDT P12_200

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 1.0342 |
| net_win_rate | 0.5458 |
| gross_profit_factor | 1.1942 |
| gross_win_rate | 0.5458 |
| sharpe_ratio | 0.2210 |
| sortino_ratio | 0.0509 |
| max_drawdown | 0.1142 |
| cagr | 0.0172 |
| net_avg_win | 96.6103 |
| net_avg_loss | -112.2670 |
| avg_hold_time_bars | 66.3386 |
| exposure | 0.7569 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
