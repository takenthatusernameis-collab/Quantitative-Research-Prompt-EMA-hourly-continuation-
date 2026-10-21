# EMA Hourly Continuation — DCR/USDT P8_26

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.5686 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -4.2792 |
| sortino_ratio | -1.6820 |
| max_drawdown | 0.8637 |
| cagr | -0.5395 |
| net_avg_win | 31.8731 |
| net_avg_loss | -49.0169 |
| avg_hold_time_bars | 6.4980 |
| exposure | 0.2238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
