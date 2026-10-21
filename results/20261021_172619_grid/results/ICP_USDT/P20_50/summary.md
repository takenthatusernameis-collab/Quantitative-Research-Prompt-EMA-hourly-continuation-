# EMA Hourly Continuation — ICP/USDT P20_50

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9183 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.3844 |
| sortino_ratio | -0.7342 |
| max_drawdown | 0.5958 |
| cagr | -0.2859 |
| net_avg_win | 59.3698 |
| net_avg_loss | -78.6147 |
| avg_hold_time_bars | 7.8427 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
