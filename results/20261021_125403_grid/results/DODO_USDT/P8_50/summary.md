# EMA Hourly Continuation — DODO/USDT P8_50

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.6716 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -3.6049 |
| sortino_ratio | -1.4297 |
| max_drawdown | 0.8146 |
| cagr | -0.4816 |
| net_avg_win | 46.2389 |
| net_avg_loss | -57.9939 |
| avg_hold_time_bars | 11.6820 |
| exposure | 0.4139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
