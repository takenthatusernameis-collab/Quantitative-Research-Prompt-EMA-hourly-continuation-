# EMA Hourly Continuation — TIA/USDT P20_26

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.8185 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.0942 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.7161 |
| sortino_ratio | -0.1313 |
| max_drawdown | 0.2102 |
| cagr | -0.0588 |
| net_avg_win | 74.9651 |
| net_avg_loss | -102.4287 |
| avg_hold_time_bars | 4.2609 |
| exposure | 0.0312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
