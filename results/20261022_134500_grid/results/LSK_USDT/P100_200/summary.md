# EMA Hourly Continuation — LSK/USDT P100_200

**Symbol:** LSK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6039 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9676 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -3.0527 |
| sortino_ratio | -0.8106 |
| max_drawdown | 0.6736 |
| cagr | -0.3270 |
| net_avg_win | 56.1853 |
| net_avg_loss | -83.7268 |
| avg_hold_time_bars | 12.6177 |
| exposure | 0.2070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
