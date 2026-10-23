# EMA Hourly Continuation — CATI/USDT P20_144

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.7954 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -4.9732 |
| sortino_ratio | -1.6074 |
| max_drawdown | 0.8161 |
| cagr | -0.5438 |
| net_avg_win | 47.6044 |
| net_avg_loss | -67.1116 |
| avg_hold_time_bars | 24.6501 |
| exposure | 0.5986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
