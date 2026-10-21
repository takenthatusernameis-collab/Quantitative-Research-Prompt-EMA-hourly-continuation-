# EMA Hourly Continuation — BSV/USDT P8_50

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.6332 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8537 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.9844 |
| sortino_ratio | -1.5650 |
| max_drawdown | 0.8405 |
| cagr | -0.5123 |
| net_avg_win | 41.0800 |
| net_avg_loss | -55.6768 |
| avg_hold_time_bars | 11.7579 |
| exposure | 0.4062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
