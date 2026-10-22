# EMA Hourly Continuation — MEW/USDT P20_50

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.7670 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9904 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.8933 |
| sortino_ratio | -0.6158 |
| max_drawdown | 0.5224 |
| cagr | -0.2465 |
| net_avg_win | 64.9126 |
| net_avg_loss | -84.9609 |
| avg_hold_time_bars | 7.4835 |
| exposure | 0.1752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
