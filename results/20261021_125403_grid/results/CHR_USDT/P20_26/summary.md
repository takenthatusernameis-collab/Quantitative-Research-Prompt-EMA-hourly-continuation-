# EMA Hourly Continuation — CHR/USDT P20_26

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9382 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.1678 |
| sortino_ratio | -0.5269 |
| max_drawdown | 0.4650 |
| cagr | -0.2141 |
| net_avg_win | 64.2215 |
| net_avg_loss | -90.9137 |
| avg_hold_time_bars | 5.8201 |
| exposure | 0.0761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
