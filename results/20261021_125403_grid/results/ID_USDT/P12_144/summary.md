# EMA Hourly Continuation — ID/USDT P12_144

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.9557 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1615 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | -0.2168 |
| sortino_ratio | -0.0613 |
| max_drawdown | 0.1649 |
| cagr | -0.0336 |
| net_avg_win | 86.0757 |
| net_avg_loss | -105.3344 |
| avg_hold_time_bars | 39.0729 |
| exposure | 0.6790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
