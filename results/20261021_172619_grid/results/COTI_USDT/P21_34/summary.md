# EMA Hourly Continuation — COTI/USDT P21_34

**Symbol:** COTI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.8102 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0768 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -1.2084 |
| sortino_ratio | -0.2968 |
| max_drawdown | 0.3765 |
| cagr | -0.1278 |
| net_avg_win | 82.6733 |
| net_avg_loss | -108.5573 |
| avg_hold_time_bars | 4.7251 |
| exposure | 0.0625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
