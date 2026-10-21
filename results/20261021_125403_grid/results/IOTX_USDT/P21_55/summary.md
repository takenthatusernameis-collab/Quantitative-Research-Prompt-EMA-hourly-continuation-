# EMA Hourly Continuation — IOTX/USDT P21_55

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.7588 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0430 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -2.1169 |
| sortino_ratio | -0.7102 |
| max_drawdown | 0.5820 |
| cagr | -0.2775 |
| net_avg_win | 63.1454 |
| net_avg_loss | -86.9708 |
| avg_hold_time_bars | 7.5055 |
| exposure | 0.1856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
