# EMA Hourly Continuation — XPR/USDT P8_89

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7777 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.8206 |
| sortino_ratio | -0.5855 |
| max_drawdown | 0.5350 |
| cagr | -0.2366 |
| net_avg_win | 69.4394 |
| net_avg_loss | -85.5003 |
| avg_hold_time_bars | 22.7475 |
| exposure | 0.5242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
