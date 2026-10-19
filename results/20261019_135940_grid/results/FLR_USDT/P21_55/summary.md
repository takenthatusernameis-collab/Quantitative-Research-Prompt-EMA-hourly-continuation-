# EMA Hourly Continuation — FLR/USDT P21_55

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.4308 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -9.9806 |
| sortino_ratio | -4.6963 |
| max_drawdown | 0.9975 |
| cagr | -0.9072 |
| net_avg_win | 16.5194 |
| net_avg_loss | -26.5916 |
| avg_hold_time_bars | 4.7159 |
| exposure | 0.2392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
