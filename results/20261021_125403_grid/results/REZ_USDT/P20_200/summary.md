# EMA Hourly Continuation — REZ/USDT P20_200

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 1.0396 |
| net_win_rate | 0.5519 |
| gross_profit_factor | 1.2177 |
| gross_win_rate | 0.5519 |
| sharpe_ratio | 0.3014 |
| sortino_ratio | 0.0809 |
| max_drawdown | 0.1784 |
| cagr | 0.0288 |
| net_avg_win | 102.7303 |
| net_avg_loss | -121.7194 |
| avg_hold_time_bars | 38.9852 |
| exposure | 0.6061 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
