# EMA Hourly Continuation — GTC/USDT P12_100

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6968 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8520 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -2.5825 |
| sortino_ratio | -0.8333 |
| max_drawdown | 0.6490 |
| cagr | -0.3185 |
| net_avg_win | 59.6840 |
| net_avg_loss | -73.0708 |
| avg_hold_time_bars | 22.6963 |
| exposure | 0.5334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
