# EMA Hourly Continuation — TIA/USDT P12_34

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1252 |
| net_profit_factor | 0.5639 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.9366 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -7.8091 |
| sortino_ratio | -3.8652 |
| max_drawdown | 0.9920 |
| cagr | -0.8522 |
| net_avg_win | 22.7360 |
| net_avg_loss | -33.0537 |
| avg_hold_time_bars | 4.2748 |
| exposure | 0.2433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
