# EMA Hourly Continuation — XPR/USDT P12_21

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9514 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.5888 |
| sortino_ratio | -0.3032 |
| max_drawdown | 0.3164 |
| cagr | -0.1299 |
| net_avg_win | 70.2709 |
| net_avg_loss | -100.7025 |
| avg_hold_time_bars | 11.7571 |
| exposure | 0.0946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
