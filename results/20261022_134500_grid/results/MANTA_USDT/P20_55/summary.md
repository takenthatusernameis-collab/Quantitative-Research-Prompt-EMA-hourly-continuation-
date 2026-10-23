# EMA Hourly Continuation — MANTA/USDT P20_55

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.5280 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8455 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -6.3430 |
| sortino_ratio | -2.7309 |
| max_drawdown | 0.9633 |
| cagr | -0.7297 |
| net_avg_win | 25.9454 |
| net_avg_loss | -39.7523 |
| avg_hold_time_bars | 6.1638 |
| exposure | 0.2600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
