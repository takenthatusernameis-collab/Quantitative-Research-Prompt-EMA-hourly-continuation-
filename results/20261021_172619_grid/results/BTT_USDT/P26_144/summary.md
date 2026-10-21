# EMA Hourly Continuation — BTT/USDT P26_144

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.5321 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.8040 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -4.0082 |
| sortino_ratio | -1.0557 |
| max_drawdown | 0.7125 |
| cagr | -0.3913 |
| net_avg_win | 54.0193 |
| net_avg_loss | -79.3134 |
| avg_hold_time_bars | 32.2339 |
| exposure | 0.5011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
