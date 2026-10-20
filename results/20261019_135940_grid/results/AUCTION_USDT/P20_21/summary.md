# EMA Hourly Continuation — AUCTION/USDT P20_21

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.1545 |
| net_win_rate | 0.2994 |
| gross_profit_factor | 0.5828 |
| gross_win_rate | 0.4107 |
| sharpe_ratio | -16.6118 |
| sortino_ratio | -8.4673 |
| max_drawdown | 1.0000 |
| cagr | -0.9906 |
| net_avg_win | 5.2642 |
| net_avg_loss | -14.5648 |
| avg_hold_time_bars | 2.6048 |
| exposure | 0.1366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
