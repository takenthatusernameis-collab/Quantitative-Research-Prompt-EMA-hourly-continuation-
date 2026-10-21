# EMA Hourly Continuation — XCN/USDT P8_34

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.7408 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.5535 |
| sortino_ratio | -0.9400 |
| max_drawdown | 0.6619 |
| cagr | -0.3507 |
| net_avg_win | 58.0418 |
| net_avg_loss | -76.0135 |
| avg_hold_time_bars | 9.3610 |
| exposure | 0.2817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
