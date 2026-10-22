# EMA Hourly Continuation — LUNA/USDT P100_144

**Symbol:** LUNA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.5999 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -2.1494 |
| sortino_ratio | -0.4650 |
| max_drawdown | 0.4221 |
| cagr | -0.1918 |
| net_avg_win | 58.0323 |
| net_avg_loss | -84.8451 |
| avg_hold_time_bars | 8.0917 |
| exposure | 0.0842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
