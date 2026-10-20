# EMA Hourly Continuation — ZETA/USDT P20_50

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.5547 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.9106 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -6.8250 |
| sortino_ratio | -2.9956 |
| max_drawdown | 0.9735 |
| cagr | -0.7621 |
| net_avg_win | 27.9959 |
| net_avg_loss | -40.8504 |
| avg_hold_time_bars | 5.5186 |
| exposure | 0.2417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
