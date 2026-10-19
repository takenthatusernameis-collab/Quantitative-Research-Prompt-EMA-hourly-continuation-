# EMA Hourly Continuation — DOGE/USDT P12_55

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.4801 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -7.6974 |
| sortino_ratio | -3.4671 |
| max_drawdown | 0.9874 |
| cagr | -0.8242 |
| net_avg_win | 19.7339 |
| net_avg_loss | -32.9688 |
| avg_hold_time_bars | 7.1821 |
| exposure | 0.3389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
