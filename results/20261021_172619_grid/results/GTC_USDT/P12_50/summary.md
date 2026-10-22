# EMA Hourly Continuation — GTC/USDT P12_50

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6960 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -3.1763 |
| sortino_ratio | -1.1620 |
| max_drawdown | 0.7529 |
| cagr | -0.4129 |
| net_avg_win | 54.4515 |
| net_avg_loss | -69.2986 |
| avg_hold_time_bars | 10.7864 |
| exposure | 0.3236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
