# EMA Hourly Continuation — W/USDT P8_100

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 1.0097 |
| net_win_rate | 0.5439 |
| gross_profit_factor | 1.1805 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | 0.1321 |
| sortino_ratio | 0.0409 |
| max_drawdown | 0.1910 |
| cagr | 0.0088 |
| net_avg_win | 92.6852 |
| net_avg_loss | -109.4443 |
| avg_hold_time_bars | 32.1557 |
| exposure | 0.6665 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
