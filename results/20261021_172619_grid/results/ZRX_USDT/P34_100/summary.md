# EMA Hourly Continuation — ZRX/USDT P34_100

**Symbol:** ZRX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7364 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -2.1526 |
| sortino_ratio | -0.6697 |
| max_drawdown | 0.5532 |
| cagr | -0.2639 |
| net_avg_win | 63.8153 |
| net_avg_loss | -85.9238 |
| avg_hold_time_bars | 14.2161 |
| exposure | 0.3050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
