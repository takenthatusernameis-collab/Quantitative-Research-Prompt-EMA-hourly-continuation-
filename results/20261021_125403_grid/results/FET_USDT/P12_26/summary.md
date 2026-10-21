# EMA Hourly Continuation — FET/USDT P12_26

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.8509 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.0934 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -0.9402 |
| sortino_ratio | -0.2654 |
| max_drawdown | 0.2790 |
| cagr | -0.1165 |
| net_avg_win | 75.9022 |
| net_avg_loss | -98.5191 |
| avg_hold_time_bars | 5.4674 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
