# EMA Hourly Continuation — TIA/USDT P89_144

**Symbol:** TIA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5472 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8266 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -4.0671 |
| sortino_ratio | -1.2062 |
| max_drawdown | 0.7677 |
| cagr | -0.4356 |
| net_avg_win | 46.7568 |
| net_avg_loss | -70.1379 |
| avg_hold_time_bars | 5.2540 |
| exposure | 0.1044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
