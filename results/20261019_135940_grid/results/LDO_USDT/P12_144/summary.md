# EMA Hourly Continuation — LDO/USDT P12_144

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5988 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8032 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -3.2496 |
| sortino_ratio | -0.9493 |
| max_drawdown | 0.6978 |
| cagr | -0.3678 |
| net_avg_win | 52.3462 |
| net_avg_loss | -70.7312 |
| avg_hold_time_bars | 35.1972 |
| exposure | 0.6975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
