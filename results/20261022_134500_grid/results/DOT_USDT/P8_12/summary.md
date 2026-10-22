# EMA Hourly Continuation — DOT/USDT P8_12

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1877 |
| net_profit_factor | 0.1445 |
| net_win_rate | 0.3495 |
| gross_profit_factor | 0.7804 |
| gross_win_rate | 0.4065 |
| sharpe_ratio | -19.8841 |
| sortino_ratio | -12.6681 |
| max_drawdown | 1.0000 |
| cagr | -0.9990 |
| net_avg_win | 2.5745 |
| net_avg_loss | -9.5732 |
| avg_hold_time_bars | 1.6473 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
