# EMA Hourly Continuation — FIL/USDT P55_89

**Symbol:** FIL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.3772 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -7.1537 |
| sortino_ratio | -2.5533 |
| max_drawdown | 0.9614 |
| cagr | -0.7213 |
| net_avg_win | 21.7667 |
| net_avg_loss | -41.5301 |
| avg_hold_time_bars | 3.7915 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
