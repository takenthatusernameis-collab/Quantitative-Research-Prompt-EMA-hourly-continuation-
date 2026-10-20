# EMA Hourly Continuation — CPOOL/USDT P55_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.5426 |
| net_win_rate | 0.4224 |
| gross_profit_factor | 0.7645 |
| gross_win_rate | 0.4276 |
| sharpe_ratio | -4.9946 |
| sortino_ratio | -1.6892 |
| max_drawdown | 0.8773 |
| cagr | -0.5555 |
| net_avg_win | 42.1018 |
| net_avg_loss | -56.7451 |
| avg_hold_time_bars | 7.6914 |
| exposure | 0.2028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
