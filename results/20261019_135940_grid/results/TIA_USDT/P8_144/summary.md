# EMA Hourly Continuation — TIA/USDT P8_144

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.7264 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9447 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -2.1157 |
| sortino_ratio | -0.6021 |
| max_drawdown | 0.5384 |
| cagr | -0.2463 |
| net_avg_win | 69.5808 |
| net_avg_loss | -88.0697 |
| avg_hold_time_bars | 42.0519 |
| exposure | 0.7741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
