# EMA Hourly Continuation — UNI/USDT P20_50

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.8959 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.4691 |
| sortino_ratio | -0.7419 |
| max_drawdown | 0.5822 |
| cagr | -0.2884 |
| net_avg_win | 59.1215 |
| net_avg_loss | -77.9391 |
| avg_hold_time_bars | 7.8826 |
| exposure | 0.1587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
