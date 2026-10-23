# EMA Hourly Continuation — ZEN/USDT P12_55

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.5498 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.8788 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -6.5631 |
| sortino_ratio | -2.9621 |
| max_drawdown | 0.9735 |
| cagr | -0.7602 |
| net_avg_win | 25.8178 |
| net_avg_loss | -37.8929 |
| avg_hold_time_bars | 8.2699 |
| exposure | 0.3872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
