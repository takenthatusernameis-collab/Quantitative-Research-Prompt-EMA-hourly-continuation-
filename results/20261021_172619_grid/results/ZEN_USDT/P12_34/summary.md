# EMA Hourly Continuation — ZEN/USDT P12_34

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.7131 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -2.7144 |
| sortino_ratio | -0.9868 |
| max_drawdown | 0.6791 |
| cagr | -0.3640 |
| net_avg_win | 53.2573 |
| net_avg_loss | -72.1759 |
| avg_hold_time_bars | 6.4403 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
