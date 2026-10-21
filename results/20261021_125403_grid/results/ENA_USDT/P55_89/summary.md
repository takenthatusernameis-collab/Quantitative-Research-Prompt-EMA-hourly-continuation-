# EMA Hourly Continuation — ENA/USDT P55_89

**Symbol:** ENA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8321 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.0208 |
| sortino_ratio | -0.4664 |
| max_drawdown | 0.4577 |
| cagr | -0.1929 |
| net_avg_win | 72.7537 |
| net_avg_loss | -89.5353 |
| avg_hold_time_bars | 6.4394 |
| exposure | 0.0773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
