# EMA Hourly Continuation — JTO/USDT P20_200

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.8257 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9466 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.0798 |
| sortino_ratio | -0.2725 |
| max_drawdown | 0.3724 |
| cagr | -0.1193 |
| net_avg_win | 84.6061 |
| net_avg_loss | -97.3708 |
| avg_hold_time_bars | 44.3854 |
| exposure | 0.6335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
