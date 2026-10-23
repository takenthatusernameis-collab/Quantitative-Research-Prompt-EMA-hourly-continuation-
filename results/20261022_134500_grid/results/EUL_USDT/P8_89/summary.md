# EMA Hourly Continuation — EUL/USDT P8_89

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.5423 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.7563 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -4.4653 |
| sortino_ratio | -1.6596 |
| max_drawdown | 0.8687 |
| cagr | -0.5499 |
| net_avg_win | 32.5444 |
| net_avg_loss | -48.5975 |
| avg_hold_time_bars | 19.3651 |
| exposure | 0.6197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
