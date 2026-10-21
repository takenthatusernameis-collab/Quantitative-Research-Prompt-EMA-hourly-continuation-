# EMA Hourly Continuation — ENA/USDT P26_89

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8628 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0114 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -0.9840 |
| sortino_ratio | -0.3006 |
| max_drawdown | 0.4061 |
| cagr | -0.1321 |
| net_avg_win | 82.1716 |
| net_avg_loss | -96.5056 |
| avg_hold_time_bars | 13.7495 |
| exposure | 0.2844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
