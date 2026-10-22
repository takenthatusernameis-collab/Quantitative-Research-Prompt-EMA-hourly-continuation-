# EMA Hourly Continuation — PIXEL/USDT P21_34

**Symbol:** PIXEL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1107 |
| net_profit_factor | 0.4295 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.8434 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -9.1414 |
| sortino_ratio | -4.3039 |
| max_drawdown | 0.9953 |
| cagr | -0.8794 |
| net_avg_win | 15.8734 |
| net_avg_loss | -27.4710 |
| avg_hold_time_bars | 3.1472 |
| exposure | 0.1577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
