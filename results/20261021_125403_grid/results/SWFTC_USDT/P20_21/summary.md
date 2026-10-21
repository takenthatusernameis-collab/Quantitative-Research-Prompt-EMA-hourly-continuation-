# EMA Hourly Continuation — SWFTC/USDT P20_21

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 134 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.3788 |
| sortino_ratio | -0.2286 |
| max_drawdown | 0.2515 |
| cagr | -0.0994 |
| net_avg_win | 77.5906 |
| net_avg_loss | -106.6007 |
| avg_hold_time_bars | 6.3657 |
| exposure | 0.0388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
