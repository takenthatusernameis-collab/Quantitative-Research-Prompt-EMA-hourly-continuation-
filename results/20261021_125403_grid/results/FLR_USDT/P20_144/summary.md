# EMA Hourly Continuation — FLR/USDT P20_144

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6851 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -2.4880 |
| sortino_ratio | -0.7601 |
| max_drawdown | 0.5980 |
| cagr | -0.2953 |
| net_avg_win | 58.9057 |
| net_avg_loss | -75.8031 |
| avg_hold_time_bars | 22.5011 |
| exposure | 0.4715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
