# EMA Hourly Continuation — TRAC/USDT P100_144

**Symbol:** TRAC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.7500 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0016 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.3071 |
| sortino_ratio | -0.2974 |
| max_drawdown | 0.3175 |
| cagr | -0.1276 |
| net_avg_win | 68.5574 |
| net_avg_loss | -93.6221 |
| avg_hold_time_bars | 6.0120 |
| exposure | 0.0686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
