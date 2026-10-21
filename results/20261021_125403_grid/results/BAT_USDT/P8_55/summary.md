# EMA Hourly Continuation — BAT/USDT P8_55

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.6929 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.0529 |
| sortino_ratio | -1.1743 |
| max_drawdown | 0.7584 |
| cagr | -0.4166 |
| net_avg_win | 47.8157 |
| net_avg_loss | -64.2333 |
| avg_hold_time_bars | 14.4490 |
| exposure | 0.4768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
