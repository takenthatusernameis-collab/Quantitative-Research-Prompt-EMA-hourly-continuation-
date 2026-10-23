# EMA Hourly Continuation — CSPR/USDT P55_144

**Symbol:** CSPR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.4316 |
| net_win_rate | 0.3880 |
| gross_profit_factor | 0.6865 |
| gross_win_rate | 0.3923 |
| sharpe_ratio | -7.0123 |
| sortino_ratio | -2.6301 |
| max_drawdown | 0.9578 |
| cagr | -0.7141 |
| net_avg_win | 26.7121 |
| net_avg_loss | -39.2423 |
| avg_hold_time_bars | 8.5321 |
| exposure | 0.2719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
