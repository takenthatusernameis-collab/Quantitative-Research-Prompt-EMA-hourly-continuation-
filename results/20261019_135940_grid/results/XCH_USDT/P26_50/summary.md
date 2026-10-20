# EMA Hourly Continuation — XCH/USDT P26_50

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.3303 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.8404 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -9.9890 |
| sortino_ratio | -4.7924 |
| max_drawdown | 0.9977 |
| cagr | -0.9113 |
| net_avg_win | 10.1858 |
| net_avg_loss | -22.0369 |
| avg_hold_time_bars | 3.2606 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
