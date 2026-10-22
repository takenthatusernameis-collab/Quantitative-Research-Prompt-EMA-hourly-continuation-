# EMA Hourly Continuation — ETC/USDT P34_89

**Symbol:** ETC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.4653 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -5.8401 |
| sortino_ratio | -2.1074 |
| max_drawdown | 0.9313 |
| cagr | -0.6496 |
| net_avg_win | 26.0603 |
| net_avg_loss | -49.0409 |
| avg_hold_time_bars | 8.1386 |
| exposure | 0.2456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
