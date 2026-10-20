# EMA Hourly Continuation — LSK/USDT P50_89

**Symbol:** LSK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.4703 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8410 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -5.5364 |
| sortino_ratio | -1.9496 |
| max_drawdown | 0.9118 |
| cagr | -0.6089 |
| net_avg_win | 29.2245 |
| net_avg_loss | -49.9715 |
| avg_hold_time_bars | 6.0162 |
| exposure | 0.1687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
