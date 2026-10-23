# EMA Hourly Continuation — GMT/USDT P20_89

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.9094 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -5.6333 |
| sortino_ratio | -2.1832 |
| max_drawdown | 0.9351 |
| cagr | -0.6528 |
| net_avg_win | 37.4793 |
| net_avg_loss | -51.8948 |
| avg_hold_time_bars | 10.4063 |
| exposure | 0.3609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
