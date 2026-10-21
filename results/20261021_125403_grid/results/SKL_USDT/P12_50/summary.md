# EMA Hourly Continuation — SKL/USDT P12_50

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 1.0096 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.3606 |
| sortino_ratio | -0.8740 |
| max_drawdown | 0.6931 |
| cagr | -0.3313 |
| net_avg_win | 73.0806 |
| net_avg_loss | -89.1588 |
| avg_hold_time_bars | 10.8597 |
| exposure | 0.3307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
