# EMA Hourly Continuation — ZRO/USDT P12_89

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.7552 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0673 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -2.1523 |
| sortino_ratio | -0.7834 |
| max_drawdown | 0.5828 |
| cagr | -0.3119 |
| net_avg_win | 56.8076 |
| net_avg_loss | -79.4973 |
| avg_hold_time_bars | 18.6488 |
| exposure | 0.5614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
