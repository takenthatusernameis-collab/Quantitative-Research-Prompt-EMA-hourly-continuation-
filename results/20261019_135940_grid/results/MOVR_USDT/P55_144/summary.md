# EMA Hourly Continuation — MOVR/USDT P55_144

**Symbol:** MOVR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8877 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -3.6024 |
| sortino_ratio | -1.1627 |
| max_drawdown | 0.7534 |
| cagr | -0.4218 |
| net_avg_win | 40.7275 |
| net_avg_loss | -62.2581 |
| avg_hold_time_bars | 10.9751 |
| exposure | 0.2604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
