# EMA Hourly Continuation — DCR/USDT P55_144

**Symbol:** DCR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6553 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.3706 |
| sortino_ratio | -0.6571 |
| max_drawdown | 0.5338 |
| cagr | -0.2610 |
| net_avg_win | 56.3847 |
| net_avg_loss | -77.4364 |
| avg_hold_time_bars | 13.4816 |
| exposure | 0.2318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
