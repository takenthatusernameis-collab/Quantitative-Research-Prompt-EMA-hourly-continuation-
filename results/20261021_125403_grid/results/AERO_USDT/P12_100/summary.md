# EMA Hourly Continuation — AERO/USDT P12_100

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 1.0115 |
| net_win_rate | 0.5431 |
| gross_profit_factor | 1.1709 |
| gross_win_rate | 0.5431 |
| sharpe_ratio | 0.1565 |
| sortino_ratio | 0.0488 |
| max_drawdown | 0.2574 |
| cagr | 0.0121 |
| net_avg_win | 107.4384 |
| net_avg_loss | -126.2638 |
| avg_hold_time_bars | 25.4461 |
| exposure | 0.5367 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
