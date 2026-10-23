# EMA Hourly Continuation — SYN/USDT P26_144

**Symbol:** SYN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.7624 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.8622 |
| sortino_ratio | -0.5662 |
| max_drawdown | 0.5169 |
| cagr | -0.2335 |
| net_avg_win | 68.2425 |
| net_avg_loss | -90.3032 |
| avg_hold_time_bars | 25.4013 |
| exposure | 0.5265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
