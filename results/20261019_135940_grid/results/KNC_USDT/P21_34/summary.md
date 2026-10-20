# EMA Hourly Continuation — KNC/USDT P21_34

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.3630 |
| net_win_rate | 0.4104 |
| gross_profit_factor | 0.9308 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -10.7282 |
| sortino_ratio | -4.9466 |
| max_drawdown | 0.9981 |
| cagr | -0.9183 |
| net_avg_win | 13.3521 |
| net_avg_loss | -25.6036 |
| avg_hold_time_bars | 3.7967 |
| exposure | 0.1791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
