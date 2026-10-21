# EMA Hourly Continuation — XCN/USDT P20_55

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6768 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.8712 |
| sortino_ratio | -0.9164 |
| max_drawdown | 0.6626 |
| cagr | -0.3441 |
| net_avg_win | 58.2055 |
| net_avg_loss | -75.9792 |
| avg_hold_time_bars | 8.6128 |
| exposure | 0.1961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
