# EMA Hourly Continuation — LINK/USDT P20_34

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.3290 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.7979 |
| gross_win_rate | 0.4165 |
| sharpe_ratio | -11.8356 |
| sortino_ratio | -5.5799 |
| max_drawdown | 0.9993 |
| cagr | -0.9445 |
| net_avg_win | 11.4470 |
| net_avg_loss | -22.4959 |
| avg_hold_time_bars | 2.6872 |
| exposure | 0.1331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
