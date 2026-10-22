# EMA Hourly Continuation — ACE/USDT P50_200

**Symbol:** ACE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.8503 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0155 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -0.8555 |
| sortino_ratio | -0.2107 |
| max_drawdown | 0.2769 |
| cagr | -0.0943 |
| net_avg_win | 83.7278 |
| net_avg_loss | -100.4770 |
| avg_hold_time_bars | 29.6465 |
| exposure | 0.3985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
