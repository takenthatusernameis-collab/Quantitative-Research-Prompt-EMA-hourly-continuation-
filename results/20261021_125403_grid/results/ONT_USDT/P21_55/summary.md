# EMA Hourly Continuation — ONT/USDT P21_55

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.8144 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.1092 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -1.5089 |
| sortino_ratio | -0.4911 |
| max_drawdown | 0.5194 |
| cagr | -0.2029 |
| net_avg_win | 71.0392 |
| net_avg_loss | -96.5653 |
| avg_hold_time_bars | 7.9688 |
| exposure | 0.1846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
