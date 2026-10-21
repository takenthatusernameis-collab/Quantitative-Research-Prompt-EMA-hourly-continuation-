# EMA Hourly Continuation — ORDI/USDT P34_89

**Symbol:** ORDI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6985 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8690 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -2.5402 |
| sortino_ratio | -0.7522 |
| max_drawdown | 0.5972 |
| cagr | -0.2918 |
| net_avg_win | 67.4723 |
| net_avg_loss | -81.8014 |
| avg_hold_time_bars | 11.3318 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
