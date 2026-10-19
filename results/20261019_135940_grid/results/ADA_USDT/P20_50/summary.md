# EMA Hourly Continuation — ADA/USDT P20_50

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.4525 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -7.2674 |
| sortino_ratio | -3.1817 |
| max_drawdown | 0.9807 |
| cagr | -0.7903 |
| net_avg_win | 18.1622 |
| net_avg_loss | -34.5607 |
| avg_hold_time_bars | 4.8568 |
| exposure | 0.2128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
