# EMA Hourly Continuation — XCN/USDT P144_200

**Symbol:** XCN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.7069 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -1.6212 |
| sortino_ratio | -0.3281 |
| max_drawdown | 0.3537 |
| cagr | -0.1408 |
| net_avg_win | 79.5891 |
| net_avg_loss | -102.9447 |
| avg_hold_time_bars | 10.1791 |
| exposure | 0.0930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
