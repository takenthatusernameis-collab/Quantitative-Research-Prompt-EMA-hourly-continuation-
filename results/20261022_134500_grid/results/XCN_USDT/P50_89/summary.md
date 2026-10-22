# EMA Hourly Continuation — XCN/USDT P50_89

**Symbol:** XCN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 837 |
| net_profit_factor | 0.3441 |
| net_win_rate | 0.3799 |
| gross_profit_factor | 0.7562 |
| gross_win_rate | 0.3943 |
| sharpe_ratio | -10.0428 |
| sortino_ratio | -4.1290 |
| max_drawdown | 0.9955 |
| cagr | -0.8827 |
| net_avg_win | 16.4185 |
| net_avg_loss | -29.2391 |
| avg_hold_time_bars | 4.0741 |
| exposure | 0.1550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
