# EMA Hourly Continuation — COMP/USDT P50_144

**Symbol:** COMP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.5274 |
| gross_profit_factor | 1.0996 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -1.0727 |
| sortino_ratio | -0.3028 |
| max_drawdown | 0.3428 |
| cagr | -0.1308 |
| net_avg_win | 69.3108 |
| net_avg_loss | -93.7435 |
| avg_hold_time_bars | 16.2193 |
| exposure | 0.2824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
