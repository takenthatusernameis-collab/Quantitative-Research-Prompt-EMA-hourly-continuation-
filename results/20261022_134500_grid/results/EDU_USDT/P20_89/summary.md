# EMA Hourly Continuation — EDU/USDT P20_89

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 769 |
| net_profit_factor | 0.6074 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8632 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -4.1119 |
| sortino_ratio | -1.6124 |
| max_drawdown | 0.8591 |
| cagr | -0.5310 |
| net_avg_win | 36.7166 |
| net_avg_loss | -52.9271 |
| avg_hold_time_bars | 11.4629 |
| exposure | 0.3989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
