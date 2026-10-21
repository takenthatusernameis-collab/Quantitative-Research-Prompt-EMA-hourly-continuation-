# EMA Hourly Continuation — XRP/USDT P12_50

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0084 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -2.7466 |
| sortino_ratio | -0.9364 |
| max_drawdown | 0.6745 |
| cagr | -0.3486 |
| net_avg_win | 56.6467 |
| net_avg_loss | -79.2581 |
| avg_hold_time_bars | 10.8726 |
| exposure | 0.2792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
