# EMA Hourly Continuation — CFX/USDT P12_20

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1507 |
| net_profit_factor | 0.2770 |
| net_win_rate | 0.3816 |
| gross_profit_factor | 0.7320 |
| gross_win_rate | 0.4074 |
| sharpe_ratio | -14.9176 |
| sortino_ratio | -8.3457 |
| max_drawdown | 1.0000 |
| cagr | -0.9870 |
| net_avg_win | 6.6632 |
| net_avg_loss | -14.8403 |
| avg_hold_time_bars | 2.1938 |
| exposure | 0.1503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
