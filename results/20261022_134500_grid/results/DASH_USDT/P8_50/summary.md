# EMA Hourly Continuation — DASH/USDT P8_50

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1136 |
| net_profit_factor | 0.4829 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -6.6485 |
| sortino_ratio | -3.1495 |
| max_drawdown | 0.9785 |
| cagr | -0.7834 |
| net_avg_win | 17.2070 |
| net_avg_loss | -31.2767 |
| avg_hold_time_bars | 8.9648 |
| exposure | 0.4629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
