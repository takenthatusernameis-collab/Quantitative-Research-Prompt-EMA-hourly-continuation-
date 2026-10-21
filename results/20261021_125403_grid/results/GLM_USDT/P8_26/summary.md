# EMA Hourly Continuation — GLM/USDT P8_26

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 852 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -4.5567 |
| sortino_ratio | -1.9046 |
| max_drawdown | 0.8905 |
| cagr | -0.5829 |
| net_avg_win | 36.5272 |
| net_avg_loss | -53.1786 |
| avg_hold_time_bars | 6.3298 |
| exposure | 0.2451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
