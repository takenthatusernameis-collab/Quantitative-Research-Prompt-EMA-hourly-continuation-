# EMA Hourly Continuation — 1INCH/USDT P20_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.7858 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.1120 |
| sortino_ratio | -0.2357 |
| max_drawdown | 0.3124 |
| cagr | -0.1035 |
| net_avg_win | 80.7694 |
| net_avg_loss | -100.9351 |
| avg_hold_time_bars | 72.9500 |
| exposure | 0.7295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
