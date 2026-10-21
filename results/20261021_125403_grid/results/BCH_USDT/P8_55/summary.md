# EMA Hourly Continuation — BCH/USDT P8_55

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6852 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9259 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.9013 |
| sortino_ratio | -1.0107 |
| max_drawdown | 0.6940 |
| cagr | -0.3703 |
| net_avg_win | 52.2876 |
| net_avg_loss | -70.8588 |
| avg_hold_time_bars | 16.8485 |
| exposure | 0.4549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
