# EMA Hourly Continuation — API3/USDT P8_20

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -3.0990 |
| sortino_ratio | -1.0804 |
| max_drawdown | 0.7142 |
| cagr | -0.3892 |
| net_avg_win | 58.1627 |
| net_avg_loss | -78.4572 |
| avg_hold_time_bars | 6.6571 |
| exposure | 0.1791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
