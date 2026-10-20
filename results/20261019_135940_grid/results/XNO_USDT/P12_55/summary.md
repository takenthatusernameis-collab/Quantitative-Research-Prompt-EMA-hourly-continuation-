# EMA Hourly Continuation — XNO/USDT P12_55

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1222 |
| net_profit_factor | 0.5257 |
| net_win_rate | 0.4092 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -8.9866 |
| sortino_ratio | -4.4292 |
| max_drawdown | 0.9957 |
| cagr | -0.8834 |
| net_avg_win | 22.0684 |
| net_avg_loss | -29.0706 |
| avg_hold_time_bars | 6.1489 |
| exposure | 0.3415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
