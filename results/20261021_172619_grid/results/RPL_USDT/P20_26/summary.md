# EMA Hourly Continuation — RPL/USDT P20_26

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6161 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.9265 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -3.2854 |
| sortino_ratio | -0.9457 |
| max_drawdown | 0.6657 |
| cagr | -0.3523 |
| net_avg_win | 55.6463 |
| net_avg_loss | -81.0332 |
| avg_hold_time_bars | 5.1256 |
| exposure | 0.0942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
