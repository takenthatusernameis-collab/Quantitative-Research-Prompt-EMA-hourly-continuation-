# EMA Hourly Continuation — DODO/USDT P8_200

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.5387 |
| net_win_rate | 0.4299 |
| gross_profit_factor | 0.8019 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -4.2884 |
| sortino_ratio | -1.3956 |
| max_drawdown | 0.8241 |
| cagr | -0.4856 |
| net_avg_win | 40.7474 |
| net_avg_loss | -57.0362 |
| avg_hold_time_bars | 30.0738 |
| exposure | 0.7376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
