# EMA Hourly Continuation — XCH/USDT P8_12

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2069 |
| net_profit_factor | 0.1330 |
| net_win_rate | 0.3354 |
| gross_profit_factor | 0.7275 |
| gross_win_rate | 0.3852 |
| sharpe_ratio | -20.5619 |
| sortino_ratio | -13.5572 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 2.2097 |
| net_avg_loss | -8.3880 |
| avg_hold_time_bars | 1.7956 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
