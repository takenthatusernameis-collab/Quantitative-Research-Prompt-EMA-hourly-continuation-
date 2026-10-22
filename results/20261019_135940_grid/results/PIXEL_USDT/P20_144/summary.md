# EMA Hourly Continuation — PIXEL/USDT P20_144

**Symbol:** PIXEL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.8104 |
| net_win_rate | 0.5160 |
| gross_profit_factor | 1.0708 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.4674 |
| sortino_ratio | -0.4359 |
| max_drawdown | 0.4995 |
| cagr | -0.1868 |
| net_avg_win | 76.8433 |
| net_avg_loss | -101.0857 |
| avg_hold_time_bars | 30.6598 |
| exposure | 0.6077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
