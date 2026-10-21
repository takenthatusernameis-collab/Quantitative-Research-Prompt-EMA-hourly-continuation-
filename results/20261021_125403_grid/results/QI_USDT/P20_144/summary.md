# EMA Hourly Continuation — QI/USDT P20_144

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7615 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9591 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.7112 |
| sortino_ratio | -0.4757 |
| max_drawdown | 0.4454 |
| cagr | -0.1970 |
| net_avg_win | 73.3331 |
| net_avg_loss | -90.9018 |
| avg_hold_time_bars | 30.1417 |
| exposure | 0.5197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
