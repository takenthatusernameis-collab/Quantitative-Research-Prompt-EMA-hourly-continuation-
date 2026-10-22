# EMA Hourly Continuation — JTO/USDT P55_144

**Symbol:** JTO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.5677 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8111 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -3.9936 |
| sortino_ratio | -1.2335 |
| max_drawdown | 0.7800 |
| cagr | -0.4445 |
| net_avg_win | 47.3522 |
| net_avg_loss | -65.6202 |
| avg_hold_time_bars | 11.2099 |
| exposure | 0.2476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
