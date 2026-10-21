# EMA Hourly Continuation — ID/USDT P8_144

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8595 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0331 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -0.8656 |
| sortino_ratio | -0.2470 |
| max_drawdown | 0.2864 |
| cagr | -0.1102 |
| net_avg_win | 76.8831 |
| net_avg_loss | -93.1202 |
| avg_hold_time_bars | 41.7714 |
| exposure | 0.7524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
