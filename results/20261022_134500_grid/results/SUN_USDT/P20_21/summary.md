# EMA Hourly Continuation — SUN/USDT P20_21

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1092 |
| net_profit_factor | 0.0501 |
| net_win_rate | 0.2179 |
| gross_profit_factor | 0.4550 |
| gross_win_rate | 0.3837 |
| sharpe_ratio | -20.2193 |
| sortino_ratio | -11.2622 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 2.2170 |
| net_avg_loss | -12.3275 |
| avg_hold_time_bars | 2.5174 |
| exposure | 0.1244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
