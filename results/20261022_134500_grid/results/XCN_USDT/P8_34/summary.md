# EMA Hourly Continuation — XCN/USDT P8_34

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1627 |
| net_profit_factor | 0.3553 |
| net_win_rate | 0.4020 |
| gross_profit_factor | 0.6951 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -12.0885 |
| sortino_ratio | -6.8697 |
| max_drawdown | 0.9998 |
| cagr | -0.9685 |
| net_avg_win | 8.4256 |
| net_avg_loss | -15.9390 |
| avg_hold_time_bars | 4.8125 |
| exposure | 0.3559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
