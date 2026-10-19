# EMA Hourly Continuation — FLR/USDT P8_12

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2076 |
| net_profit_factor | 0.1151 |
| net_win_rate | 0.2967 |
| gross_profit_factor | 0.5027 |
| gross_win_rate | 0.3776 |
| sharpe_ratio | -22.9770 |
| sortino_ratio | -15.5653 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 2.1111 |
| net_avg_loss | -7.7400 |
| avg_hold_time_bars | 1.8025 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
