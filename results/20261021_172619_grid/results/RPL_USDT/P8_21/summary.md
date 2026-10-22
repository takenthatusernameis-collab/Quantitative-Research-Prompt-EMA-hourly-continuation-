# EMA Hourly Continuation — RPL/USDT P8_21

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.7941 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.1213 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -2.4637 |
| sortino_ratio | -0.9910 |
| max_drawdown | 0.7183 |
| cagr | -0.3662 |
| net_avg_win | 64.7515 |
| net_avg_loss | -87.5687 |
| avg_hold_time_bars | 5.9364 |
| exposure | 0.2112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
