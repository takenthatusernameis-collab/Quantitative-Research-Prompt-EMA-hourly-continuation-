# EMA Hourly Continuation — DGB/USDT P12_34

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.7266 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9858 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.7644 |
| sortino_ratio | -0.9240 |
| max_drawdown | 0.6878 |
| cagr | -0.3457 |
| net_avg_win | 65.9644 |
| net_avg_loss | -84.6917 |
| avg_hold_time_bars | 6.7349 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
