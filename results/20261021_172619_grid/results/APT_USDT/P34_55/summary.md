# EMA Hourly Continuation — APT/USDT P34_55

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8052 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.1057 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -1.1126 |
| sortino_ratio | -0.2712 |
| max_drawdown | 0.3041 |
| cagr | -0.1173 |
| net_avg_win | 74.1210 |
| net_avg_loss | -102.2803 |
| avg_hold_time_bars | 5.3298 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
