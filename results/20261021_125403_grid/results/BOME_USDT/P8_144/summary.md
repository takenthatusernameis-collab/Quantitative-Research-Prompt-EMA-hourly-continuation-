# EMA Hourly Continuation — BOME/USDT P8_144

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8701 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 0.9978 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -0.7523 |
| sortino_ratio | -0.2033 |
| max_drawdown | 0.3044 |
| cagr | -0.0922 |
| net_avg_win | 80.2783 |
| net_avg_loss | -93.8275 |
| avg_hold_time_bars | 45.8123 |
| exposure | 0.7434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
