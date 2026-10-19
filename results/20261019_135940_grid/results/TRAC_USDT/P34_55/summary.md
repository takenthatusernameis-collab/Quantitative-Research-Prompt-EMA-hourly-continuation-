# EMA Hourly Continuation — TRAC/USDT P34_55

**Symbol:** TRAC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.3800 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -7.5404 |
| sortino_ratio | -2.9620 |
| max_drawdown | 0.9767 |
| cagr | -0.7720 |
| net_avg_win | 17.7947 |
| net_avg_loss | -35.7612 |
| avg_hold_time_bars | 4.4652 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
