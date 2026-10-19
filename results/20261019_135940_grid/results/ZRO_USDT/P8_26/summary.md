# EMA Hourly Continuation — ZRO/USDT P8_26

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1443 |
| net_profit_factor | 0.5483 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -8.6585 |
| sortino_ratio | -4.7939 |
| max_drawdown | 0.9961 |
| cagr | -0.9053 |
| net_avg_win | 18.3474 |
| net_avg_loss | -28.1250 |
| avg_hold_time_bars | 3.8531 |
| exposure | 0.2721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
