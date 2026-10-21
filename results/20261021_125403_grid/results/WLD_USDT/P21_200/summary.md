# EMA Hourly Continuation — WLD/USDT P21_200

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 1.0863 |
| net_win_rate | 0.5500 |
| gross_profit_factor | 1.2117 |
| gross_win_rate | 0.5500 |
| sharpe_ratio | 0.4617 |
| sortino_ratio | 0.1082 |
| max_drawdown | 0.1180 |
| cagr | 0.0426 |
| net_avg_win | 97.2530 |
| net_avg_loss | -109.4180 |
| avg_hold_time_bars | 54.0346 |
| exposure | 0.6386 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
