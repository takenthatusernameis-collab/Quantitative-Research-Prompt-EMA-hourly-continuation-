# EMA Hourly Continuation — SEI/USDT P55_144

**Symbol:** SEI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -3.3528 |
| sortino_ratio | -0.9975 |
| max_drawdown | 0.7073 |
| cagr | -0.3802 |
| net_avg_win | 51.6369 |
| net_avg_loss | -73.5803 |
| avg_hold_time_bars | 12.6013 |
| exposure | 0.2572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
