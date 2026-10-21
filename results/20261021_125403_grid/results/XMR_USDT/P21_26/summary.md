# EMA Hourly Continuation — XMR/USDT P21_26

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 87 |
| net_profit_factor | 0.4953 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.7008 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -1.9878 |
| sortino_ratio | -0.2645 |
| max_drawdown | 0.2914 |
| cagr | -0.1152 |
| net_avg_win | 72.1612 |
| net_avg_loss | -102.8435 |
| avg_hold_time_bars | 4.3103 |
| exposure | 0.0170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
