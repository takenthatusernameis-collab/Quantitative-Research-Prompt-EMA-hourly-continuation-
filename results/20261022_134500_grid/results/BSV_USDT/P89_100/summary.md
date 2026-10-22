# EMA Hourly Continuation — BSV/USDT P89_100

**Symbol:** BSV/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.2536 |
| net_win_rate | 0.3486 |
| gross_profit_factor | 0.8552 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -11.0868 |
| sortino_ratio | -4.1583 |
| max_drawdown | 0.9967 |
| cagr | -0.8959 |
| net_avg_win | 14.8547 |
| net_avg_loss | -31.3446 |
| avg_hold_time_bars | 2.3792 |
| exposure | 0.0707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
