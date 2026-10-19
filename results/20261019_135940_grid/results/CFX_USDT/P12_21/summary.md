# EMA Hourly Continuation — CFX/USDT P12_21

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1490 |
| net_profit_factor | 0.2767 |
| net_win_rate | 0.3745 |
| gross_profit_factor | 0.7172 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -14.7185 |
| sortino_ratio | -8.1882 |
| max_drawdown | 1.0000 |
| cagr | -0.9852 |
| net_avg_win | 6.8565 |
| net_avg_loss | -14.8344 |
| avg_hold_time_bars | 2.3081 |
| exposure | 0.1563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
