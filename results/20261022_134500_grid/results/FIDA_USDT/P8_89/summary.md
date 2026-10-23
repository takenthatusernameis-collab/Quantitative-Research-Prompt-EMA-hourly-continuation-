# EMA Hourly Continuation — FIDA/USDT P8_89

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.5474 |
| net_win_rate | 0.4616 |
| gross_profit_factor | 0.8095 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -4.2676 |
| sortino_ratio | -1.6167 |
| max_drawdown | 0.8605 |
| cagr | -0.5372 |
| net_avg_win | 30.7449 |
| net_avg_loss | -48.1661 |
| avg_hold_time_bars | 19.2411 |
| exposure | 0.6356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
