# EMA Hourly Continuation — MTL/USDT P8_21

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1466 |
| net_profit_factor | 0.3748 |
| net_win_rate | 0.4168 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -11.7829 |
| sortino_ratio | -6.3938 |
| max_drawdown | 0.9997 |
| cagr | -0.9590 |
| net_avg_win | 9.8105 |
| net_avg_loss | -18.7030 |
| avg_hold_time_bars | 4.4168 |
| exposure | 0.2930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
