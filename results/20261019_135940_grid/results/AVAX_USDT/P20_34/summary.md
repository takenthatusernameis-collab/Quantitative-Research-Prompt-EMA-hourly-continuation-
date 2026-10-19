# EMA Hourly Continuation — AVAX/USDT P20_34

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.4162 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.9712 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -10.9655 |
| sortino_ratio | -5.1970 |
| max_drawdown | 0.9989 |
| cagr | -0.9321 |
| net_avg_win | 15.2831 |
| net_avg_loss | -26.4865 |
| avg_hold_time_bars | 2.4883 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
