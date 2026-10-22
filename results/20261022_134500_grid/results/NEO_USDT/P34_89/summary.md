# EMA Hourly Continuation — NEO/USDT P34_89

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.4474 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8347 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -6.1978 |
| sortino_ratio | -2.3068 |
| max_drawdown | 0.9435 |
| cagr | -0.6788 |
| net_avg_win | 24.4479 |
| net_avg_loss | -43.2753 |
| avg_hold_time_bars | 7.9363 |
| exposure | 0.2547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
