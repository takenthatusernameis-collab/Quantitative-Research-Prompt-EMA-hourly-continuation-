# EMA Hourly Continuation — XCH/USDT P55_100

**Symbol:** XCH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6859 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -1.9876 |
| sortino_ratio | -0.5157 |
| max_drawdown | 0.4476 |
| cagr | -0.2105 |
| net_avg_win | 61.4820 |
| net_avg_loss | -83.8342 |
| avg_hold_time_bars | 8.8723 |
| exposure | 0.1327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
