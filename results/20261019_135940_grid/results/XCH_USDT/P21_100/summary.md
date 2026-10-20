# EMA Hourly Continuation — XCH/USDT P21_100

**Symbol:** XCH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.5930 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -3.8367 |
| sortino_ratio | -1.4772 |
| max_drawdown | 0.8393 |
| cagr | -0.5099 |
| net_avg_win | 32.9028 |
| net_avg_loss | -53.1761 |
| avg_hold_time_bars | 13.3103 |
| exposure | 0.4562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
