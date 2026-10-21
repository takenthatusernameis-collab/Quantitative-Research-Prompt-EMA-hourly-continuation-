# EMA Hourly Continuation — ETH/USDT P8_144

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7909 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0365 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.1159 |
| sortino_ratio | -0.2531 |
| max_drawdown | 0.2795 |
| cagr | -0.1098 |
| net_avg_win | 75.4153 |
| net_avg_loss | -98.4596 |
| avg_hold_time_bars | 69.0920 |
| exposure | 0.7851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
