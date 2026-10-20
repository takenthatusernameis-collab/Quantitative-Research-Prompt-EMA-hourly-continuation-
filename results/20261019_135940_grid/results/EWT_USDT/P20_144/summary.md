# EMA Hourly Continuation — EWT/USDT P20_144

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.5165 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.7463 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -4.8768 |
| sortino_ratio | -1.6369 |
| max_drawdown | 0.8824 |
| cagr | -0.5511 |
| net_avg_win | 37.7753 |
| net_avg_loss | -52.8535 |
| avg_hold_time_bars | 16.7860 |
| exposure | 0.4456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
