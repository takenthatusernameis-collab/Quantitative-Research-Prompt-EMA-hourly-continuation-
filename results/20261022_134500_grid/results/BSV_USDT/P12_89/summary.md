# EMA Hourly Continuation — BSV/USDT P12_89

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.4786 |
| net_win_rate | 0.4102 |
| gross_profit_factor | 0.7772 |
| gross_win_rate | 0.4223 |
| sharpe_ratio | -7.3305 |
| sortino_ratio | -2.9332 |
| max_drawdown | 0.9755 |
| cagr | -0.7684 |
| net_avg_win | 26.4698 |
| net_avg_loss | -38.4627 |
| avg_hold_time_bars | 14.5862 |
| exposure | 0.5463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
