# EMA Hourly Continuation — LSK/USDT P20_144

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6514 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9109 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -2.9517 |
| sortino_ratio | -0.8967 |
| max_drawdown | 0.6662 |
| cagr | -0.3477 |
| net_avg_win | 56.1416 |
| net_avg_loss | -76.4170 |
| avg_hold_time_bars | 25.1202 |
| exposure | 0.5321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
