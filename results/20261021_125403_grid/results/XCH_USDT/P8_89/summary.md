# EMA Hourly Continuation — XCH/USDT P8_89

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.8063 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -1.5718 |
| sortino_ratio | -0.5518 |
| max_drawdown | 0.4862 |
| cagr | -0.2262 |
| net_avg_win | 65.6348 |
| net_avg_loss | -81.6788 |
| avg_hold_time_bars | 22.0266 |
| exposure | 0.6017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
