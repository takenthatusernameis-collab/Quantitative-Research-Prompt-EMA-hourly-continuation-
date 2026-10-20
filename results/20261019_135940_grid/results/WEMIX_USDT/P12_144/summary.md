# EMA Hourly Continuation — WEMIX/USDT P12_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.3322 |
| net_win_rate | 0.3217 |
| gross_profit_factor | 0.5032 |
| gross_win_rate | 0.3315 |
| sharpe_ratio | -9.6141 |
| sortino_ratio | -3.6509 |
| max_drawdown | 0.9895 |
| cagr | -0.8360 |
| net_avg_win | 21.3085 |
| net_avg_loss | -30.4221 |
| avg_hold_time_bars | 21.4680 |
| exposure | 0.7006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
