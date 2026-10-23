# EMA Hourly Continuation — POLYX/USDT P20_144

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7183 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 1.0125 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.3316 |
| sortino_ratio | -0.7204 |
| max_drawdown | 0.5985 |
| cagr | -0.2898 |
| net_avg_win | 61.7758 |
| net_avg_loss | -84.2315 |
| avg_hold_time_bars | 25.0062 |
| exposure | 0.5467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
