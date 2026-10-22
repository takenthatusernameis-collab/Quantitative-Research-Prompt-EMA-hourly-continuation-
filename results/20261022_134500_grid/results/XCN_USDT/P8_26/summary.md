# EMA Hourly Continuation — XCN/USDT P8_26

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1797 |
| net_profit_factor | 0.2759 |
| net_win_rate | 0.3929 |
| gross_profit_factor | 0.6001 |
| gross_win_rate | 0.4112 |
| sharpe_ratio | -13.9542 |
| sortino_ratio | -8.3518 |
| max_drawdown | 1.0000 |
| cagr | -0.9859 |
| net_avg_win | 5.3959 |
| net_avg_loss | -12.6575 |
| avg_hold_time_bars | 3.5921 |
| exposure | 0.2934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
