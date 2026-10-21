# EMA Hourly Continuation — LUNC/USDT P12_50

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6066 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.8015 |
| gross_win_rate | 0.4350 |
| sharpe_ratio | -4.1489 |
| sortino_ratio | -1.4430 |
| max_drawdown | 0.8159 |
| cagr | -0.4852 |
| net_avg_win | 47.9321 |
| net_avg_loss | -60.8359 |
| avg_hold_time_bars | 10.3633 |
| exposure | 0.2826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
