# EMA Hourly Continuation — XYO/USDT P8_26

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.6014 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8540 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -4.9342 |
| sortino_ratio | -1.8697 |
| max_drawdown | 0.8880 |
| cagr | -0.5774 |
| net_avg_win | 42.3100 |
| net_avg_loss | -56.5676 |
| avg_hold_time_bars | 6.9140 |
| exposure | 0.2218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
