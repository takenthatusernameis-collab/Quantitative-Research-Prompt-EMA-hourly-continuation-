# EMA Hourly Continuation — GTC/USDT P8_89

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.7555 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -2.2074 |
| sortino_ratio | -0.7363 |
| max_drawdown | 0.5980 |
| cagr | -0.2877 |
| net_avg_win | 67.6227 |
| net_avg_loss | -81.4277 |
| avg_hold_time_bars | 23.9655 |
| exposure | 0.5991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
