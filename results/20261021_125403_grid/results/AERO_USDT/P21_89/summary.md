# EMA Hourly Continuation — AERO/USDT P21_89

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.8741 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0429 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -0.8937 |
| sortino_ratio | -0.2716 |
| max_drawdown | 0.3485 |
| cagr | -0.1207 |
| net_avg_win | 83.6997 |
| net_avg_loss | -100.1221 |
| avg_hold_time_bars | 16.0424 |
| exposure | 0.3267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
