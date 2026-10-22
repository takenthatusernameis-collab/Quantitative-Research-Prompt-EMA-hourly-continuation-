# EMA Hourly Continuation — ENA/USDT P12_55

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.7138 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -3.2232 |
| sortino_ratio | -1.4109 |
| max_drawdown | 0.8343 |
| cagr | -0.4868 |
| net_avg_win | 42.4896 |
| net_avg_loss | -59.2798 |
| avg_hold_time_bars | 8.5335 |
| exposure | 0.3708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
