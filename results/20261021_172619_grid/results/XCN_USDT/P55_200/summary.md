# EMA Hourly Continuation — XCN/USDT P55_200

**Symbol:** XCN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8611 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -2.0193 |
| sortino_ratio | -0.4986 |
| max_drawdown | 0.4573 |
| cagr | -0.2060 |
| net_avg_win | 72.8676 |
| net_avg_loss | -89.5608 |
| avg_hold_time_bars | 25.3696 |
| exposure | 0.3494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
