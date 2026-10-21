# EMA Hourly Continuation — ARB/USDT P8_50

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.7943 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0001 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.6380 |
| sortino_ratio | -0.5898 |
| max_drawdown | 0.5304 |
| cagr | -0.2392 |
| net_avg_win | 60.2925 |
| net_avg_loss | -77.3692 |
| avg_hold_time_bars | 15.5635 |
| exposure | 0.4457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
