# EMA Hourly Continuation — XMR/USDT P8_34

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6046 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8304 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -3.7657 |
| sortino_ratio | -1.2787 |
| max_drawdown | 0.7744 |
| cagr | -0.4432 |
| net_avg_win | 45.9965 |
| net_avg_loss | -62.2273 |
| avg_hold_time_bars | 8.2214 |
| exposure | 0.2126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
