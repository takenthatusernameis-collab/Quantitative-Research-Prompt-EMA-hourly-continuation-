# EMA Hourly Continuation — ERG/USDT P20_144

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -2.2433 |
| sortino_ratio | -0.6390 |
| max_drawdown | 0.5308 |
| cagr | -0.2549 |
| net_avg_win | 59.6755 |
| net_avg_loss | -75.5733 |
| avg_hold_time_bars | 26.0423 |
| exposure | 0.4759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
