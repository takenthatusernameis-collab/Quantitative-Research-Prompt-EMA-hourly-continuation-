# EMA Hourly Continuation — MNT/USDT P20_21

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1224 |
| net_profit_factor | 0.0919 |
| net_win_rate | 0.2377 |
| gross_profit_factor | 0.5821 |
| gross_win_rate | 0.3636 |
| sharpe_ratio | -20.3971 |
| sortino_ratio | -11.4425 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 3.4790 |
| net_avg_loss | -11.8032 |
| avg_hold_time_bars | 1.8105 |
| exposure | 0.1007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
