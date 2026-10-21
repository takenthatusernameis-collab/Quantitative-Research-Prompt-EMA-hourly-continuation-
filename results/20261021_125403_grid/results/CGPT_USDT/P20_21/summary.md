# EMA Hourly Continuation — CGPT/USDT P20_21

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -1.0755 |
| sortino_ratio | -0.1763 |
| max_drawdown | 0.2045 |
| cagr | -0.0773 |
| net_avg_win | 75.6367 |
| net_avg_loss | -106.5923 |
| avg_hold_time_bars | 4.9615 |
| exposure | 0.0293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
