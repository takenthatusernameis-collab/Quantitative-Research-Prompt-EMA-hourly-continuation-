# EMA Hourly Continuation — XCN/USDT P8_200

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.5803 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8612 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -4.0982 |
| sortino_ratio | -1.3495 |
| max_drawdown | 0.8059 |
| cagr | -0.4791 |
| net_avg_win | 44.2084 |
| net_avg_loss | -63.7766 |
| avg_hold_time_bars | 30.2857 |
| exposure | 0.7613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
