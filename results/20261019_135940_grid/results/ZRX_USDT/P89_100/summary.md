# EMA Hourly Continuation — ZRX/USDT P89_100

**Symbol:** ZRX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.3011 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -9.5227 |
| sortino_ratio | -3.4582 |
| max_drawdown | 0.9889 |
| cagr | -0.8334 |
| net_avg_win | 17.4600 |
| net_avg_loss | -36.8469 |
| avg_hold_time_bars | 2.6513 |
| exposure | 0.0757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
