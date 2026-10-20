# EMA Hourly Continuation — MASK/USDT P21_89

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.4591 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.7730 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -6.0699 |
| sortino_ratio | -2.2905 |
| max_drawdown | 0.9414 |
| cagr | -0.6681 |
| net_avg_win | 25.8356 |
| net_avg_loss | -42.5816 |
| avg_hold_time_bars | 12.6280 |
| exposure | 0.4104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
