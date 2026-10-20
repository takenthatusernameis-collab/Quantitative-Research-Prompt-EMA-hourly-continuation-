# EMA Hourly Continuation — UQC/USDT P20_200

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.3139 |
| net_win_rate | 0.2906 |
| gross_profit_factor | 0.4191 |
| gross_win_rate | 0.2956 |
| sharpe_ratio | -4.8557 |
| sortino_ratio | -0.9625 |
| max_drawdown | 0.6911 |
| cagr | -0.3723 |
| net_avg_win | 53.5996 |
| net_avg_loss | -69.9532 |
| avg_hold_time_bars | 79.0936 |
| exposure | 0.7267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
