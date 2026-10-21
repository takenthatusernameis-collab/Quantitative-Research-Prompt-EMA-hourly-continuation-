# EMA Hourly Continuation — REZ/USDT P8_89

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.9823 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.1483 |
| gross_win_rate | 0.5373 |
| sharpe_ratio | -0.0659 |
| sortino_ratio | -0.0219 |
| max_drawdown | 0.3005 |
| cagr | -0.0199 |
| net_avg_win | 96.1848 |
| net_avg_loss | -113.6931 |
| avg_hold_time_bars | 25.6329 |
| exposure | 0.6185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
