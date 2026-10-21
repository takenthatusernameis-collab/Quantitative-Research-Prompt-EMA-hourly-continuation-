# EMA Hourly Continuation — XCN/USDT P8_20

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6671 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9290 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.7438 |
| sortino_ratio | -0.7960 |
| max_drawdown | 0.6017 |
| cagr | -0.3055 |
| net_avg_win | 61.3176 |
| net_avg_loss | -83.4004 |
| avg_hold_time_bars | 6.8495 |
| exposure | 0.1283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
