# EMA Hourly Continuation — XMR/USDT P89_200

**Symbol:** XMR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7259 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.8245 |
| sortino_ratio | -0.4668 |
| max_drawdown | 0.4692 |
| cagr | -0.1918 |
| net_avg_win | 70.3109 |
| net_avg_loss | -92.7038 |
| avg_hold_time_bars | 10.7492 |
| exposure | 0.1559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
