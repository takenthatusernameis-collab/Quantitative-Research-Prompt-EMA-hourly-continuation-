# EMA Hourly Continuation — LISTA/USDT P8_55

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 872 |
| net_profit_factor | 0.6269 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9123 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -4.7013 |
| sortino_ratio | -2.0236 |
| max_drawdown | 0.8967 |
| cagr | -0.6178 |
| net_avg_win | 36.9994 |
| net_avg_loss | -51.4219 |
| avg_hold_time_bars | 11.7339 |
| exposure | 0.5003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
