# EMA Hourly Continuation — WLD/USDT P21_89

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 1.0365 |
| net_win_rate | 0.5535 |
| gross_profit_factor | 1.2253 |
| gross_win_rate | 0.5535 |
| sharpe_ratio | 0.3089 |
| sortino_ratio | 0.0941 |
| max_drawdown | 0.2355 |
| cagr | 0.0326 |
| net_avg_win | 97.9932 |
| net_avg_loss | -117.2154 |
| avg_hold_time_bars | 17.6811 |
| exposure | 0.3528 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
