# EMA Hourly Continuation — ENA/USDT P8_12

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 1.1329 |
| net_win_rate | 0.5943 |
| gross_profit_factor | 1.4500 |
| gross_win_rate | 0.5943 |
| sharpe_ratio | 0.5527 |
| sortino_ratio | 0.1078 |
| max_drawdown | 0.1400 |
| cagr | 0.0433 |
| net_avg_win | 92.0771 |
| net_avg_loss | -119.0534 |
| avg_hold_time_bars | 4.9086 |
| exposure | 0.0390 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
