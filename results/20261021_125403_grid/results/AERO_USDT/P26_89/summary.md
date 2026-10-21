# EMA Hourly Continuation — AERO/USDT P26_89

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8439 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0151 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.1063 |
| sortino_ratio | -0.3230 |
| max_drawdown | 0.3587 |
| cagr | -0.1401 |
| net_avg_win | 81.5705 |
| net_avg_loss | -98.0719 |
| avg_hold_time_bars | 13.7084 |
| exposure | 0.2586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
