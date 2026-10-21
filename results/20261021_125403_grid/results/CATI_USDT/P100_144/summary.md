# EMA Hourly Continuation — CATI/USDT P100_144

**Symbol:** CATI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.5684 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.7541 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -2.4948 |
| sortino_ratio | -0.5027 |
| max_drawdown | 0.4036 |
| cagr | -0.2066 |
| net_avg_win | 69.9541 |
| net_avg_loss | -93.2755 |
| avg_hold_time_bars | 10.1856 |
| exposure | 0.0932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
