# EMA Hourly Continuation — TFUEL/USDT P12_34

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5867 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.8324 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -5.2444 |
| sortino_ratio | -1.9563 |
| max_drawdown | 0.8995 |
| cagr | -0.5932 |
| net_avg_win | 42.8462 |
| net_avg_loss | -55.4765 |
| avg_hold_time_bars | 6.2616 |
| exposure | 0.1949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
