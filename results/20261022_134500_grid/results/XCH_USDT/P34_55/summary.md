# EMA Hourly Continuation — XCH/USDT P34_55

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.3134 |
| net_win_rate | 0.4058 |
| gross_profit_factor | 0.8525 |
| gross_win_rate | 0.4310 |
| sharpe_ratio | -9.9669 |
| sortino_ratio | -4.6343 |
| max_drawdown | 0.9971 |
| cagr | -0.9012 |
| net_avg_win | 10.4632 |
| net_avg_loss | -22.7969 |
| avg_hold_time_bars | 2.9384 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
