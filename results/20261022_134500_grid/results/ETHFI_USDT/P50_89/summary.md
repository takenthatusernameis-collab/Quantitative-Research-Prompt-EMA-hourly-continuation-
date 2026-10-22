# EMA Hourly Continuation — ETHFI/USDT P50_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5013 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8262 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -5.5977 |
| sortino_ratio | -2.1121 |
| max_drawdown | 0.9242 |
| cagr | -0.6397 |
| net_avg_win | 28.9060 |
| net_avg_loss | -46.9764 |
| avg_hold_time_bars | 4.1357 |
| exposure | 0.1344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
