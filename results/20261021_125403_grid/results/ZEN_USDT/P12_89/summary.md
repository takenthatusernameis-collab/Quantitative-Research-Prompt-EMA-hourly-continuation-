# EMA Hourly Continuation — ZEN/USDT P12_89

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7491 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9204 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.0779 |
| sortino_ratio | -0.6662 |
| max_drawdown | 0.5429 |
| cagr | -0.2653 |
| net_avg_win | 66.2206 |
| net_avg_loss | -81.3667 |
| avg_hold_time_bars | 23.3452 |
| exposure | 0.5380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
