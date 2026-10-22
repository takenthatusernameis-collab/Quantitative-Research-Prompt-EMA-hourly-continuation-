# EMA Hourly Continuation — XCN/USDT P20_21

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1465 |
| net_profit_factor | 0.0887 |
| net_win_rate | 0.2328 |
| gross_profit_factor | 0.4078 |
| gross_win_rate | 0.3051 |
| sharpe_ratio | -21.9303 |
| sortino_ratio | -12.9979 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 2.8541 |
| net_avg_loss | -9.7627 |
| avg_hold_time_bars | 1.6669 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
