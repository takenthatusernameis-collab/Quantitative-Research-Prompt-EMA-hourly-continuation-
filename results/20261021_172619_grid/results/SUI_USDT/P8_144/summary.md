# EMA Hourly Continuation — SUI/USDT P8_144

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.9520 |
| net_win_rate | 0.5325 |
| gross_profit_factor | 1.1241 |
| gross_win_rate | 0.5325 |
| sharpe_ratio | -0.2279 |
| sortino_ratio | -0.0645 |
| max_drawdown | 0.2031 |
| cagr | -0.0353 |
| net_avg_win | 83.5810 |
| net_avg_loss | -99.9849 |
| avg_hold_time_bars | 38.9403 |
| exposure | 0.6815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
