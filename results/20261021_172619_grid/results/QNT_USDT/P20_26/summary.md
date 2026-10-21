# EMA Hourly Continuation — QNT/USDT P20_26

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.7730 |
| net_win_rate | 0.5398 |
| gross_profit_factor | 1.1530 |
| gross_win_rate | 0.5398 |
| sharpe_ratio | -0.9856 |
| sortino_ratio | -0.1896 |
| max_drawdown | 0.1953 |
| cagr | -0.0829 |
| net_avg_win | 70.0082 |
| net_avg_loss | -106.2137 |
| avg_hold_time_bars | 4.8466 |
| exposure | 0.0388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
