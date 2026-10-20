# EMA Hourly Continuation — ZIL/USDT P89_144

**Symbol:** ZIL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.4430 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.8715 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -5.0693 |
| sortino_ratio | -1.6336 |
| max_drawdown | 0.8669 |
| cagr | -0.5494 |
| net_avg_win | 29.0232 |
| net_avg_loss | -55.8562 |
| avg_hold_time_bars | 4.9728 |
| exposure | 0.1164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
