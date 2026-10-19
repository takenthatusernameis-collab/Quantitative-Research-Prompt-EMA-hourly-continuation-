# EMA Hourly Continuation — RAY/USDT P12_26

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1373 |
| net_profit_factor | 0.4899 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -9.4528 |
| sortino_ratio | -4.9368 |
| max_drawdown | 0.9979 |
| cagr | -0.9132 |
| net_avg_win | 15.8388 |
| net_avg_loss | -25.4700 |
| avg_hold_time_bars | 3.0277 |
| exposure | 0.1890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
