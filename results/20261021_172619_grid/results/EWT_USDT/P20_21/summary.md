# EMA Hourly Continuation — EWT/USDT P20_21

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.5009 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.6934 |
| gross_win_rate | 0.4141 |
| sharpe_ratio | -2.3606 |
| sortino_ratio | -0.3784 |
| max_drawdown | 0.3847 |
| cagr | -0.1624 |
| net_avg_win | 68.0139 |
| net_avg_loss | -95.9534 |
| avg_hold_time_bars | 8.2188 |
| exposure | 0.0478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
