# EMA Hourly Continuation — DUSK/USDT P12_26

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6853 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.1256 |
| sortino_ratio | -1.0451 |
| max_drawdown | 0.7173 |
| cagr | -0.3821 |
| net_avg_win | 59.2074 |
| net_avg_loss | -76.5986 |
| avg_hold_time_bars | 5.5683 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
