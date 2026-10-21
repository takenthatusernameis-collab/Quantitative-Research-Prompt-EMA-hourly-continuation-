# EMA Hourly Continuation — FET/USDT P8_34

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.8767 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0813 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -1.1681 |
| sortino_ratio | -0.4369 |
| max_drawdown | 0.5029 |
| cagr | -0.1862 |
| net_avg_win | 82.0273 |
| net_avg_loss | -100.4561 |
| avg_hold_time_bars | 8.6849 |
| exposure | 0.2669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
