# EMA Hourly Continuation — XEC/USDT P100_200

**Symbol:** XEC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.6080 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8452 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -2.6448 |
| sortino_ratio | -0.6407 |
| max_drawdown | 0.5373 |
| cagr | -0.2551 |
| net_avg_win | 61.1354 |
| net_avg_loss | -85.1870 |
| avg_hold_time_bars | 11.9828 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
