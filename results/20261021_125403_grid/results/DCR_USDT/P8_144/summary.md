# EMA Hourly Continuation — DCR/USDT P8_144

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7796 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9676 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.6821 |
| sortino_ratio | -0.5488 |
| max_drawdown | 0.4930 |
| cagr | -0.2240 |
| net_avg_win | 64.2770 |
| net_avg_loss | -80.8973 |
| avg_hold_time_bars | 27.9619 |
| exposure | 0.6643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
