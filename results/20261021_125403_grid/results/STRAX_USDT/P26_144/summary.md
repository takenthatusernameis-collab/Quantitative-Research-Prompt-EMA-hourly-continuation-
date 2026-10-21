# EMA Hourly Continuation — STRAX/USDT P26_144

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.7975 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -3.8896 |
| sortino_ratio | -1.2541 |
| max_drawdown | 0.7686 |
| cagr | -0.4399 |
| net_avg_win | 54.2144 |
| net_avg_loss | -67.7798 |
| avg_hold_time_bars | 17.1764 |
| exposure | 0.4052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
