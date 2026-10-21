# EMA Hourly Continuation — BTT/USDT P8_144

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6419 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.8802 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.2212 |
| sortino_ratio | -0.5312 |
| max_drawdown | 0.4955 |
| cagr | -0.2175 |
| net_avg_win | 61.5013 |
| net_avg_loss | -86.7525 |
| avg_hold_time_bars | 62.2624 |
| exposure | 0.7981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
