# EMA Hourly Continuation — CVX/USDT P55_100

**Symbol:** CVX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.5516 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -4.6375 |
| sortino_ratio | -1.5821 |
| max_drawdown | 0.8566 |
| cagr | -0.5353 |
| net_avg_win | 38.6254 |
| net_avg_loss | -60.4660 |
| avg_hold_time_bars | 5.8433 |
| exposure | 0.1559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
