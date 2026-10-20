# EMA Hourly Continuation — CKB/USDT P20_26

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1236 |
| net_profit_factor | 0.2057 |
| net_win_rate | 0.3608 |
| gross_profit_factor | 0.5389 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -14.5301 |
| sortino_ratio | -7.4264 |
| max_drawdown | 0.9999 |
| cagr | -0.9793 |
| net_avg_win | 5.8048 |
| net_avg_loss | -15.9346 |
| avg_hold_time_bars | 2.0049 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
