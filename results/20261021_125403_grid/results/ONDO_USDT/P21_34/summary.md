# EMA Hourly Continuation — ONDO/USDT P21_34

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.7782 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0377 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.2420 |
| sortino_ratio | -0.2767 |
| max_drawdown | 0.3229 |
| cagr | -0.1193 |
| net_avg_win | 78.5765 |
| net_avg_loss | -104.3969 |
| avg_hold_time_bars | 5.8875 |
| exposure | 0.0642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
