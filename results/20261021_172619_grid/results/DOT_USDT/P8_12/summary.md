# EMA Hourly Continuation — DOT/USDT P8_12

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.8159 |
| net_win_rate | 0.5412 |
| gross_profit_factor | 1.1846 |
| gross_win_rate | 0.5412 |
| sharpe_ratio | -0.8869 |
| sortino_ratio | -0.1792 |
| max_drawdown | 0.2517 |
| cagr | -0.0787 |
| net_avg_win | 78.5235 |
| net_avg_loss | -113.5365 |
| avg_hold_time_bars | 4.6237 |
| exposure | 0.0408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
