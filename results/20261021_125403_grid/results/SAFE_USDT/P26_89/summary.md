# EMA Hourly Continuation — SAFE/USDT P26_89

**Symbol:** SAFE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.9425 |
| net_win_rate | 0.5427 |
| gross_profit_factor | 1.1786 |
| gross_win_rate | 0.5427 |
| sharpe_ratio | -0.3728 |
| sortino_ratio | -0.1157 |
| max_drawdown | 0.2615 |
| cagr | -0.0579 |
| net_avg_win | 91.3487 |
| net_avg_loss | -115.0031 |
| avg_hold_time_bars | 15.2079 |
| exposure | 0.3183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
