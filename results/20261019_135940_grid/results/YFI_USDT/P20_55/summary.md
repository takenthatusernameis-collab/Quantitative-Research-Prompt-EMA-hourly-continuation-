# EMA Hourly Continuation — YFI/USDT P20_55

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.4615 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 1.0468 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -9.3942 |
| sortino_ratio | -4.3778 |
| max_drawdown | 0.9964 |
| cagr | -0.8900 |
| net_avg_win | 17.8636 |
| net_avg_loss | -29.9362 |
| avg_hold_time_bars | 5.0703 |
| exposure | 0.2515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
