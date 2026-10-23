# EMA Hourly Continuation — WEMIX/USDT P12_20

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2023 |
| net_profit_factor | 0.1145 |
| net_win_rate | 0.2308 |
| gross_profit_factor | 0.3568 |
| gross_win_rate | 0.2729 |
| sharpe_ratio | -25.0193 |
| sortino_ratio | -16.7916 |
| max_drawdown | 1.0000 |
| cagr | -0.9999 |
| net_avg_win | 2.7676 |
| net_avg_loss | -7.2574 |
| avg_hold_time_bars | 2.2699 |
| exposure | 0.2087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
