# EMA Hourly Continuation — BABYDOGE/USDT P100_144

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 13 |
| net_profit_factor | 1.4324 |
| net_win_rate | 0.6154 |
| gross_profit_factor | 1.5794 |
| gross_win_rate | 0.6154 |
| sharpe_ratio | 0.4171 |
| sortino_ratio | 0.0224 |
| max_drawdown | 0.0130 |
| cagr | 0.0092 |
| net_avg_win | 97.2731 |
| net_avg_loss | -108.6559 |
| avg_hold_time_bars | 15.3077 |
| exposure | 0.0090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
