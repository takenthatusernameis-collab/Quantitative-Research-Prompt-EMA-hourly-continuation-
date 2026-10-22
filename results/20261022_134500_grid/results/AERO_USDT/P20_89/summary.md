# EMA Hourly Continuation — AERO/USDT P20_89

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.7356 |
| net_win_rate | 0.4992 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -2.5684 |
| sortino_ratio | -0.9167 |
| max_drawdown | 0.6671 |
| cagr | -0.3500 |
| net_avg_win | 58.3919 |
| net_avg_loss | -79.1255 |
| avg_hold_time_bars | 12.9984 |
| exposure | 0.3728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
