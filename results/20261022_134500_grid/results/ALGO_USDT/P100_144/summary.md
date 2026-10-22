# EMA Hourly Continuation — ALGO/USDT P100_144

**Symbol:** ALGO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.4800 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8982 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -4.8015 |
| sortino_ratio | -1.4697 |
| max_drawdown | 0.8464 |
| cagr | -0.5160 |
| net_avg_win | 34.8574 |
| net_avg_loss | -64.2300 |
| avg_hold_time_bars | 3.7696 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
