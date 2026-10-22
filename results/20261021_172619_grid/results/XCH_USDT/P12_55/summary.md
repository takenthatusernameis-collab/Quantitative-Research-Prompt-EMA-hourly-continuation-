# EMA Hourly Continuation — XCH/USDT P12_55

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6605 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8574 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -3.1912 |
| sortino_ratio | -1.1964 |
| max_drawdown | 0.7566 |
| cagr | -0.4237 |
| net_avg_win | 45.1382 |
| net_avg_loss | -59.6580 |
| avg_hold_time_bars | 10.8672 |
| exposure | 0.3423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
