# EMA Hourly Continuation — ILV/USDT P12_26

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6759 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -2.5753 |
| sortino_ratio | -0.8370 |
| max_drawdown | 0.6455 |
| cagr | -0.3175 |
| net_avg_win | 50.4401 |
| net_avg_loss | -74.0499 |
| avg_hold_time_bars | 5.6465 |
| exposure | 0.1314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
