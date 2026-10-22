# EMA Hourly Continuation — XCN/USDT P12_20

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1778 |
| net_profit_factor | 0.1953 |
| net_win_rate | 0.3245 |
| gross_profit_factor | 0.5343 |
| gross_win_rate | 0.3616 |
| sharpe_ratio | -18.5957 |
| sortino_ratio | -11.3062 |
| max_drawdown | 1.0000 |
| cagr | -0.9976 |
| net_avg_win | 4.2054 |
| net_avg_loss | -10.3468 |
| avg_hold_time_bars | 2.0208 |
| exposure | 0.1633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
