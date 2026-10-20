# EMA Hourly Continuation — TFUEL/USDT P8_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.5056 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4224 |
| sharpe_ratio | -9.4383 |
| sortino_ratio | -4.7570 |
| max_drawdown | 0.9973 |
| cagr | -0.9034 |
| net_avg_win | 19.0299 |
| net_avg_loss | -26.5777 |
| avg_hold_time_bars | 7.5892 |
| exposure | 0.4447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
