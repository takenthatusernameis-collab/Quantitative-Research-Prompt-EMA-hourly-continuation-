# EMA Hourly Continuation — WAVES/USDT P34_144

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7295 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9663 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -1.9098 |
| sortino_ratio | -0.5567 |
| max_drawdown | 0.4950 |
| cagr | -0.2262 |
| net_avg_win | 62.1430 |
| net_avg_loss | -83.9669 |
| avg_hold_time_bars | 19.4530 |
| exposure | 0.3670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
