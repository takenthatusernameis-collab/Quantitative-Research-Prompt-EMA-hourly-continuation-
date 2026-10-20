# EMA Hourly Continuation — XEC/USDT P26_89

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.5543 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.9562 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -5.5463 |
| sortino_ratio | -2.2123 |
| max_drawdown | 0.9353 |
| cagr | -0.6542 |
| net_avg_win | 31.5658 |
| net_avg_loss | -48.1529 |
| avg_hold_time_bars | 8.9800 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
