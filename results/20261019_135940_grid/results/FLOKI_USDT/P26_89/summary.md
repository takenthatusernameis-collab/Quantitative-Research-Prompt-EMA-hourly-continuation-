# EMA Hourly Continuation — FLOKI/USDT P26_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6225 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -4.2655 |
| sortino_ratio | -1.5965 |
| max_drawdown | 0.8624 |
| cagr | -0.5346 |
| net_avg_win | 42.3932 |
| net_avg_loss | -60.4526 |
| avg_hold_time_bars | 11.2493 |
| exposure | 0.3610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
