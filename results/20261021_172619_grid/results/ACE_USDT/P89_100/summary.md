# EMA Hourly Continuation — ACE/USDT P89_100

**Symbol:** ACE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.5705 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.3782 |
| sortino_ratio | -0.4665 |
| max_drawdown | 0.4443 |
| cagr | -0.1928 |
| net_avg_win | 63.0310 |
| net_avg_loss | -97.2176 |
| avg_hold_time_bars | 6.2766 |
| exposure | 0.0534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
