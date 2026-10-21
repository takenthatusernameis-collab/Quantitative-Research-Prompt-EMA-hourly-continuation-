# EMA Hourly Continuation — DUSK/USDT P21_26

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.5879 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8426 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -2.5153 |
| sortino_ratio | -0.5445 |
| max_drawdown | 0.4747 |
| cagr | -0.2225 |
| net_avg_win | 63.6497 |
| net_avg_loss | -90.9444 |
| avg_hold_time_bars | 4.3783 |
| exposure | 0.0458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
