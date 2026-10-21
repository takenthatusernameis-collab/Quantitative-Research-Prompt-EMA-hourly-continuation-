# EMA Hourly Continuation — ONDO/USDT P12_21

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.7767 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0427 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -1.2159 |
| sortino_ratio | -0.2745 |
| max_drawdown | 0.3236 |
| cagr | -0.1182 |
| net_avg_win | 74.7945 |
| net_avg_loss | -101.1143 |
| avg_hold_time_bars | 5.7480 |
| exposure | 0.0643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
