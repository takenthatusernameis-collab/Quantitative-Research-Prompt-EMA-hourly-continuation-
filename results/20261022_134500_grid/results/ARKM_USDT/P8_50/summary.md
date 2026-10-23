# EMA Hourly Continuation — ARKM/USDT P8_50

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.6423 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9332 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -4.9100 |
| sortino_ratio | -2.2674 |
| max_drawdown | 0.9358 |
| cagr | -0.6606 |
| net_avg_win | 32.8092 |
| net_avg_loss | -46.2808 |
| avg_hold_time_bars | 10.0986 |
| exposure | 0.4935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
