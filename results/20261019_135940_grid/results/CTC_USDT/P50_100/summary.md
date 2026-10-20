# EMA Hourly Continuation — CTC/USDT P50_100

**Symbol:** CTC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.3919 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.7763 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -6.5605 |
| sortino_ratio | -2.3096 |
| max_drawdown | 0.9478 |
| cagr | -0.6859 |
| net_avg_win | 22.6468 |
| net_avg_loss | -42.8265 |
| avg_hold_time_bars | 6.3354 |
| exposure | 0.1820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
