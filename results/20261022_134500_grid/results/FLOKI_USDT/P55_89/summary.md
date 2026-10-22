# EMA Hourly Continuation — FLOKI/USDT P55_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.5393 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9188 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -5.6262 |
| sortino_ratio | -2.1420 |
| max_drawdown | 0.9284 |
| cagr | -0.6430 |
| net_avg_win | 32.4062 |
| net_avg_loss | -51.5968 |
| avg_hold_time_bars | 4.2766 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
