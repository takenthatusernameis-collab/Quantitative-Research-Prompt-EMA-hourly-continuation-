# EMA Hourly Continuation — MOVR/USDT P21_144

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.5319 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7793 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -4.3570 |
| sortino_ratio | -1.5053 |
| max_drawdown | 0.8420 |
| cagr | -0.5128 |
| net_avg_win | 35.6907 |
| net_avg_loss | -51.8893 |
| avg_hold_time_bars | 18.4230 |
| exposure | 0.5108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
