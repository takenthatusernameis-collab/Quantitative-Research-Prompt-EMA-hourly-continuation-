# EMA Hourly Continuation — MANTA/USDT P21_55

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.7059 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9103 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -2.5853 |
| sortino_ratio | -0.8404 |
| max_drawdown | 0.6287 |
| cagr | -0.3199 |
| net_avg_win | 60.2821 |
| net_avg_loss | -77.5439 |
| avg_hold_time_bars | 9.1522 |
| exposure | 0.2159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
