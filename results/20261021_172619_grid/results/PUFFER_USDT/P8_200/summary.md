# EMA Hourly Continuation — PUFFER/USDT P8_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.9660 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0879 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -0.1327 |
| sortino_ratio | -0.0319 |
| max_drawdown | 0.1825 |
| cagr | -0.0194 |
| net_avg_win | 93.8886 |
| net_avg_loss | -106.2754 |
| avg_hold_time_bars | 62.9062 |
| exposure | 0.7974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
