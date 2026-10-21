# EMA Hourly Continuation — BCH/USDT P20_21

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 113 |
| net_profit_factor | 0.6458 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.3703 |
| sortino_ratio | -0.2095 |
| max_drawdown | 0.2389 |
| cagr | -0.0905 |
| net_avg_win | 69.0242 |
| net_avg_loss | -105.0046 |
| avg_hold_time_bars | 5.8407 |
| exposure | 0.0300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
