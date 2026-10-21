# EMA Hourly Continuation — ADA/USDT P12_144

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.8303 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0250 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.0617 |
| sortino_ratio | -0.2758 |
| max_drawdown | 0.3142 |
| cagr | -0.1203 |
| net_avg_win | 80.6320 |
| net_avg_loss | -100.1087 |
| avg_hold_time_bars | 45.0304 |
| exposure | 0.6734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
