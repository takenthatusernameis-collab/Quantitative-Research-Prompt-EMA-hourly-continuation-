# EMA Hourly Continuation — TRX/USDT P8_26

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1320 |
| net_profit_factor | 0.1638 |
| net_win_rate | 0.3265 |
| gross_profit_factor | 0.8666 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -17.7294 |
| sortino_ratio | -9.8102 |
| max_drawdown | 1.0000 |
| cagr | -0.9954 |
| net_avg_win | 4.5465 |
| net_avg_loss | -13.4528 |
| avg_hold_time_bars | 4.3742 |
| exposure | 0.2625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
