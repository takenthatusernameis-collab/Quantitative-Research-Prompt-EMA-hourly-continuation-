# EMA Hourly Continuation — SATS/USDT P12_34

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0173 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.1296 |
| sortino_ratio | -0.7515 |
| max_drawdown | 0.5942 |
| cagr | -0.2938 |
| net_avg_win | 68.0277 |
| net_avg_loss | -86.6132 |
| avg_hold_time_bars | 7.3301 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
