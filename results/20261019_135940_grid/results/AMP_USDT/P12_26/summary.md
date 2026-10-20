# EMA Hourly Continuation — AMP/USDT P12_26

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1814 |
| net_profit_factor | 0.2185 |
| net_win_rate | 0.3379 |
| gross_profit_factor | 0.5757 |
| gross_win_rate | 0.3760 |
| sharpe_ratio | -17.7693 |
| sortino_ratio | -10.8560 |
| max_drawdown | 1.0000 |
| cagr | -0.9965 |
| net_avg_win | 4.5600 |
| net_avg_loss | -10.6538 |
| avg_hold_time_bars | 2.6863 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
