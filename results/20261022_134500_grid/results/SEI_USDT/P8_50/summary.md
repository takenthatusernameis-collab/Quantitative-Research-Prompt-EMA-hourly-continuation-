# EMA Hourly Continuation — SEI/USDT P8_50

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -5.5977 |
| sortino_ratio | -2.5692 |
| max_drawdown | 0.9586 |
| cagr | -0.7136 |
| net_avg_win | 33.0979 |
| net_avg_loss | -47.0343 |
| avg_hold_time_bars | 9.8650 |
| exposure | 0.4816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
