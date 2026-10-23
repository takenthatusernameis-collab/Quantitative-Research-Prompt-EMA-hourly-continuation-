# EMA Hourly Continuation — ERG/USDT P20_89

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.4313 |
| net_win_rate | 0.4218 |
| gross_profit_factor | 0.6776 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -6.4257 |
| sortino_ratio | -2.4948 |
| max_drawdown | 0.9540 |
| cagr | -0.7036 |
| net_avg_win | 22.5114 |
| net_avg_loss | -38.0782 |
| avg_hold_time_bars | 10.4336 |
| exposure | 0.3609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
