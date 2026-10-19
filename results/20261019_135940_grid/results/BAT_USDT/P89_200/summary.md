# EMA Hourly Continuation — BAT/USDT P89_200

**Symbol:** BAT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.5217 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.4259 |
| sortino_ratio | -0.9751 |
| max_drawdown | 0.6967 |
| cagr | -0.3695 |
| net_avg_win | 39.3826 |
| net_avg_loss | -67.6548 |
| avg_hold_time_bars | 9.3706 |
| exposure | 0.1712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
