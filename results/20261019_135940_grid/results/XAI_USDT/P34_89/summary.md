# EMA Hourly Continuation — XAI/USDT P34_89

**Symbol:** XAI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.6580 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -4.6727 |
| sortino_ratio | -1.7682 |
| max_drawdown | 0.8973 |
| cagr | -0.5704 |
| net_avg_win | 50.0921 |
| net_avg_loss | -66.8391 |
| avg_hold_time_bars | 8.7289 |
| exposure | 0.2869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
