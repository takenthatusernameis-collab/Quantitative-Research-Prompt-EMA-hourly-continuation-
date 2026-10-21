# EMA Hourly Continuation — SYN/USDT P20_144

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.9475 |
| net_win_rate | 0.5266 |
| gross_profit_factor | 1.1079 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -0.2591 |
| sortino_ratio | -0.0686 |
| max_drawdown | 0.1497 |
| cagr | -0.0363 |
| net_avg_win | 89.8598 |
| net_avg_loss | -105.5055 |
| avg_hold_time_bars | 38.4349 |
| exposure | 0.5905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
