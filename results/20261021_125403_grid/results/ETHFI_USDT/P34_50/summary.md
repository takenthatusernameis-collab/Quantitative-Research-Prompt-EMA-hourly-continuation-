# EMA Hourly Continuation — ETHFI/USDT P34_50

**Symbol:** ETHFI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.7051 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -1.6765 |
| sortino_ratio | -0.3695 |
| max_drawdown | 0.3588 |
| cagr | -0.1560 |
| net_avg_win | 72.7341 |
| net_avg_loss | -94.8350 |
| avg_hold_time_bars | 6.3319 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
