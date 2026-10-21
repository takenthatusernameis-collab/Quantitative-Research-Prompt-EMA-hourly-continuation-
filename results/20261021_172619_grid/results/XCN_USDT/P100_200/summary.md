# EMA Hourly Continuation — XCN/USDT P100_200

**Symbol:** XCN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.7414 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9387 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.6025 |
| sortino_ratio | -0.3715 |
| max_drawdown | 0.3921 |
| cagr | -0.1578 |
| net_avg_win | 79.0695 |
| net_avg_loss | -98.8678 |
| avg_hold_time_bars | 16.1326 |
| exposure | 0.1936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
