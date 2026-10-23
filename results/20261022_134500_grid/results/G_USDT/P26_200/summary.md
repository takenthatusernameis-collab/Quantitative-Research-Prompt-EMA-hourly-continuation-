# EMA Hourly Continuation — G/USDT P26_200

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.5068 |
| net_win_rate | 0.4209 |
| gross_profit_factor | 0.7208 |
| gross_win_rate | 0.4272 |
| sharpe_ratio | -3.9075 |
| sortino_ratio | -1.0449 |
| max_drawdown | 0.6916 |
| cagr | -0.3946 |
| net_avg_win | 51.2784 |
| net_avg_loss | -73.5319 |
| avg_hold_time_bars | 36.1709 |
| exposure | 0.6010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
