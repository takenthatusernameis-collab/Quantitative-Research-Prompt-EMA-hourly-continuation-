# EMA Hourly Continuation — RIO/USDT P50_144

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7019 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -2.0563 |
| sortino_ratio | -0.5475 |
| max_drawdown | 0.5138 |
| cagr | -0.2235 |
| net_avg_win | 70.0329 |
| net_avg_loss | -80.7433 |
| avg_hold_time_bars | 13.6097 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
