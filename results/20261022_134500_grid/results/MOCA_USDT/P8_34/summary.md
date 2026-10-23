# EMA Hourly Continuation — MOCA/USDT P8_34

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1222 |
| net_profit_factor | 0.4937 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8227 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -8.7412 |
| sortino_ratio | -4.5058 |
| max_drawdown | 0.9939 |
| cagr | -0.8918 |
| net_avg_win | 17.9446 |
| net_avg_loss | -28.7783 |
| avg_hold_time_bars | 5.3789 |
| exposure | 0.3295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
