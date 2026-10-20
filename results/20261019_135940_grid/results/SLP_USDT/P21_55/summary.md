# EMA Hourly Continuation — SLP/USDT P21_55

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.5302 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -8.6137 |
| sortino_ratio | -4.0205 |
| max_drawdown | 0.9930 |
| cagr | -0.8573 |
| net_avg_win | 24.9473 |
| net_avg_loss | -33.5334 |
| avg_hold_time_bars | 5.0871 |
| exposure | 0.2495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
