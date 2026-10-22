# EMA Hourly Continuation — ZEN/USDT P8_34

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1442 |
| net_profit_factor | 0.4674 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -8.4776 |
| sortino_ratio | -4.5087 |
| max_drawdown | 0.9962 |
| cagr | -0.8911 |
| net_avg_win | 13.4720 |
| net_avg_loss | -23.5879 |
| avg_hold_time_bars | 5.2926 |
| exposure | 0.3469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
