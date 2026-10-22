# EMA Hourly Continuation — SSV/USDT P12_144

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8402 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -2.0955 |
| sortino_ratio | -0.5630 |
| max_drawdown | 0.5137 |
| cagr | -0.2290 |
| net_avg_win | 72.5782 |
| net_avg_loss | -84.4171 |
| avg_hold_time_bars | 42.1989 |
| exposure | 0.6913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
