# EMA Hourly Continuation — ETH/USDT P50_55

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 777 |
| net_profit_factor | 0.0902 |
| net_win_rate | 0.2587 |
| gross_profit_factor | 0.7831 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -15.2180 |
| sortino_ratio | -6.7601 |
| max_drawdown | 0.9999 |
| cagr | -0.9774 |
| net_avg_win | 4.9351 |
| net_avg_loss | -19.0820 |
| avg_hold_time_bars | 1.8327 |
| exposure | 0.0647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
