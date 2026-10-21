# EMA Hourly Continuation — ZEN/USDT P8_89

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7434 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9000 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -2.0504 |
| sortino_ratio | -0.6750 |
| max_drawdown | 0.5561 |
| cagr | -0.2690 |
| net_avg_win | 61.6355 |
| net_avg_loss | -76.0772 |
| avg_hold_time_bars | 25.6056 |
| exposure | 0.6227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
