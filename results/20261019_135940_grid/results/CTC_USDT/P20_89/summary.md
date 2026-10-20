# EMA Hourly Continuation — CTC/USDT P20_89

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5436 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -5.2822 |
| sortino_ratio | -2.0010 |
| max_drawdown | 0.9256 |
| cagr | -0.6308 |
| net_avg_win | 32.0665 |
| net_avg_loss | -50.4148 |
| avg_hold_time_bars | 11.8527 |
| exposure | 0.3987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
