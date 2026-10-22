# EMA Hourly Continuation — CGPT/USDT P20_144

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.9171 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0845 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -0.5091 |
| sortino_ratio | -0.1400 |
| max_drawdown | 0.2856 |
| cagr | -0.0665 |
| net_avg_win | 92.3083 |
| net_avg_loss | -109.2839 |
| avg_hold_time_bars | 31.9041 |
| exposure | 0.5293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
