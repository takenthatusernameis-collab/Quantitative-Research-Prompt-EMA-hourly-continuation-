# EMA Hourly Continuation — FIL/USDT P89_144

**Symbol:** FIL/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7839 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0602 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -1.0925 |
| sortino_ratio | -0.2376 |
| max_drawdown | 0.2900 |
| cagr | -0.1040 |
| net_avg_win | 74.0797 |
| net_avg_loss | -101.3734 |
| avg_hold_time_bars | 7.5789 |
| exposure | 0.0785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
