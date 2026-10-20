# EMA Hourly Continuation — XCH/USDT P8_55

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1197 |
| net_profit_factor | 0.4766 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -7.3617 |
| sortino_ratio | -3.5621 |
| max_drawdown | 0.9883 |
| cagr | -0.8266 |
| net_avg_win | 17.1617 |
| net_avg_loss | -28.0387 |
| avg_hold_time_bars | 9.2865 |
| exposure | 0.5053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
