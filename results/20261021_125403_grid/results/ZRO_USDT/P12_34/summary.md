# EMA Hourly Continuation — ZRO/USDT P12_34

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.9220 |
| net_win_rate | 0.5398 |
| gross_profit_factor | 1.1578 |
| gross_win_rate | 0.5398 |
| sharpe_ratio | -0.5146 |
| sortino_ratio | -0.1732 |
| max_drawdown | 0.3382 |
| cagr | -0.0828 |
| net_avg_win | 79.6006 |
| net_avg_loss | -101.2836 |
| avg_hold_time_bars | 7.3267 |
| exposure | 0.1800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
