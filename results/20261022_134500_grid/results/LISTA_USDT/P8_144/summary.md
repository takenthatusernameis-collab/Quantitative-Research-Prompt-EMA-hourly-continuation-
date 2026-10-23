# EMA Hourly Continuation — LISTA/USDT P8_144

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7543 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9895 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.9616 |
| sortino_ratio | -0.6300 |
| max_drawdown | 0.5026 |
| cagr | -0.2544 |
| net_avg_win | 65.0653 |
| net_avg_loss | -83.7581 |
| avg_hold_time_bars | 30.2253 |
| exposure | 0.7020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
