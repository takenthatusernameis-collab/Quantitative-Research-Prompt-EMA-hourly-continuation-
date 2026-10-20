# EMA Hourly Continuation — LISTA/USDT P20_50

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 839 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -5.8752 |
| sortino_ratio | -2.5004 |
| max_drawdown | 0.9359 |
| cagr | -0.6918 |
| net_avg_win | 32.4062 |
| net_avg_loss | -46.3609 |
| avg_hold_time_bars | 5.8868 |
| exposure | 0.2415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
