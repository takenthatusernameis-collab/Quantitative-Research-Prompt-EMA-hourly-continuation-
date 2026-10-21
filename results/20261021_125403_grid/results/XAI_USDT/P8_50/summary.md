# EMA Hourly Continuation — XAI/USDT P8_50

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.7961 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.5026 |
| sortino_ratio | -0.9769 |
| max_drawdown | 0.7414 |
| cagr | -0.3635 |
| net_avg_win | 73.1883 |
| net_avg_loss | -85.7688 |
| avg_hold_time_bars | 13.0920 |
| exposure | 0.4463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
