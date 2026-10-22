# EMA Hourly Continuation — ACE/USDT P12_200

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.8452 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -0.8775 |
| sortino_ratio | -0.2088 |
| max_drawdown | 0.2979 |
| cagr | -0.0931 |
| net_avg_win | 85.1509 |
| net_avg_loss | -101.4765 |
| avg_hold_time_bars | 59.1971 |
| exposure | 0.7474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
