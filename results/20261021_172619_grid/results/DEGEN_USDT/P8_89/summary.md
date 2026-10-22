# EMA Hourly Continuation — DEGEN/USDT P8_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.9059 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0409 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -0.7357 |
| sortino_ratio | -0.2320 |
| max_drawdown | 0.3651 |
| cagr | -0.1061 |
| net_avg_win | 95.9001 |
| net_avg_loss | -109.8854 |
| avg_hold_time_bars | 29.0538 |
| exposure | 0.6389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
