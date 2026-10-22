# EMA Hourly Continuation — ILV/USDT P21_89

**Symbol:** ILV/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7938 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0026 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.7880 |
| sortino_ratio | -0.5827 |
| max_drawdown | 0.5451 |
| cagr | -0.2352 |
| net_avg_win | 73.1214 |
| net_avg_loss | -91.4079 |
| avg_hold_time_bars | 14.6023 |
| exposure | 0.3438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
