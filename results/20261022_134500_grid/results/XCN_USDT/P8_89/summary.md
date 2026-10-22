# EMA Hourly Continuation — XCN/USDT P8_89

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.4558 |
| net_win_rate | 0.4250 |
| gross_profit_factor | 0.7525 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -7.7924 |
| sortino_ratio | -3.4717 |
| max_drawdown | 0.9877 |
| cagr | -0.8243 |
| net_avg_win | 19.1874 |
| net_avg_loss | -31.1200 |
| avg_hold_time_bars | 12.4014 |
| exposure | 0.5716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
