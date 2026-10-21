# EMA Hourly Continuation — RLC/USDT P34_100

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7565 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0015 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -1.9313 |
| sortino_ratio | -0.6039 |
| max_drawdown | 0.5422 |
| cagr | -0.2425 |
| net_avg_win | 65.2767 |
| net_avg_loss | -87.0139 |
| avg_hold_time_bars | 11.9853 |
| exposure | 0.2593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
