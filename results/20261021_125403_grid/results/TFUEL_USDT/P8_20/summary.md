# EMA Hourly Continuation — TFUEL/USDT P8_20

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5514 |
| net_win_rate | 0.4155 |
| gross_profit_factor | 0.8127 |
| gross_win_rate | 0.4155 |
| sharpe_ratio | -5.9091 |
| sortino_ratio | -2.1201 |
| max_drawdown | 0.9179 |
| cagr | -0.6261 |
| net_avg_win | 42.8338 |
| net_avg_loss | -55.2142 |
| avg_hold_time_bars | 5.4976 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
