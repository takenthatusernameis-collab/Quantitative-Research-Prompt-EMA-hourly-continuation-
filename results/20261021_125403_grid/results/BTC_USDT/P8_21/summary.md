# EMA Hourly Continuation — BTC/USDT P8_21

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.5110 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -4.4335 |
| sortino_ratio | -1.3967 |
| max_drawdown | 0.8415 |
| cagr | -0.4742 |
| net_avg_win | 32.8917 |
| net_avg_loss | -63.4147 |
| avg_hold_time_bars | 6.6022 |
| exposure | 0.1421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
