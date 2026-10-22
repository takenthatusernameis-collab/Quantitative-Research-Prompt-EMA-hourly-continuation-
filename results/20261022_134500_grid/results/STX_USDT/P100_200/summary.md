# EMA Hourly Continuation — STX/USDT P100_200

**Symbol:** STX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6834 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.1280 |
| gross_win_rate | 0.5319 |
| sharpe_ratio | -2.3204 |
| sortino_ratio | -0.6084 |
| max_drawdown | 0.5456 |
| cagr | -0.2642 |
| net_avg_win | 61.8617 |
| net_avg_loss | -98.3728 |
| avg_hold_time_bars | 9.8421 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
