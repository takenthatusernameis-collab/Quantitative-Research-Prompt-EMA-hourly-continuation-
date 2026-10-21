# EMA Hourly Continuation — WOO/USDT P12_21

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7308 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0353 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -2.2862 |
| sortino_ratio | -0.6835 |
| max_drawdown | 0.5639 |
| cagr | -0.2691 |
| net_avg_win | 68.1701 |
| net_avg_loss | -93.7094 |
| avg_hold_time_bars | 4.8799 |
| exposure | 0.0960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
