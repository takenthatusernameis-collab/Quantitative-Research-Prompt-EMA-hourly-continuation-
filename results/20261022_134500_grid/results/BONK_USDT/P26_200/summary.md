# EMA Hourly Continuation — BONK/USDT P26_200

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6556 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.5232 |
| sortino_ratio | -0.6845 |
| max_drawdown | 0.6196 |
| cagr | -0.2816 |
| net_avg_win | 60.3310 |
| net_avg_loss | -82.7312 |
| avg_hold_time_bars | 34.2819 |
| exposure | 0.5859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
