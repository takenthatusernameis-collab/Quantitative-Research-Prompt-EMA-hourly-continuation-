# EMA Hourly Continuation — ENA/USDT P8_21

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1651 |
| net_profit_factor | 0.4769 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8175 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -9.2132 |
| sortino_ratio | -5.2727 |
| max_drawdown | 0.9985 |
| cagr | -0.9243 |
| net_avg_win | 12.1350 |
| net_avg_loss | -21.1831 |
| avg_hold_time_bars | 2.8783 |
| exposure | 0.2160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
