# EMA Hourly Continuation — STRK/USDT P8_89

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8766 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0399 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -0.8459 |
| sortino_ratio | -0.2684 |
| max_drawdown | 0.3063 |
| cagr | -0.1201 |
| net_avg_win | 77.7748 |
| net_avg_loss | -93.5702 |
| avg_hold_time_bars | 28.4479 |
| exposure | 0.6323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
