# EMA Hourly Continuation — JUP/USDT P89_144

**Symbol:** JUP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.4387 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7246 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -5.5904 |
| sortino_ratio | -1.7064 |
| max_drawdown | 0.8823 |
| cagr | -0.5706 |
| net_avg_win | 35.2874 |
| net_avg_loss | -56.6230 |
| avg_hold_time_bars | 5.0318 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
