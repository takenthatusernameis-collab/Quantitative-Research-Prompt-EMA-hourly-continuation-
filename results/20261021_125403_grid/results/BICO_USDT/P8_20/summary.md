# EMA Hourly Continuation — BICO/USDT P8_20

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 766 |
| net_profit_factor | 0.7242 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0125 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.7680 |
| sortino_ratio | -1.1003 |
| max_drawdown | 0.7304 |
| cagr | -0.3962 |
| net_avg_win | 48.7256 |
| net_avg_loss | -68.7059 |
| avg_hold_time_bars | 5.5679 |
| exposure | 0.1939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
