# EMA Hourly Continuation — SSV/USDT P55_144

**Symbol:** SSV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.5792 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -4.3643 |
| sortino_ratio | -1.4487 |
| max_drawdown | 0.8299 |
| cagr | -0.4959 |
| net_avg_win | 45.0971 |
| net_avg_loss | -64.0763 |
| avg_hold_time_bars | 10.4335 |
| exposure | 0.2625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
