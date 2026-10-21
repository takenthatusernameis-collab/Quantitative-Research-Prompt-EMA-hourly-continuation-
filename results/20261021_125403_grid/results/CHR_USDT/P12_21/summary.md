# EMA Hourly Continuation — CHR/USDT P12_21

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 1.0066 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.6413 |
| sortino_ratio | -0.8225 |
| max_drawdown | 0.6488 |
| cagr | -0.3136 |
| net_avg_win | 65.3373 |
| net_avg_loss | -88.3293 |
| avg_hold_time_bars | 5.3383 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
