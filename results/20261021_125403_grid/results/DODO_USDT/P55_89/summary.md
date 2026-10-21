# EMA Hourly Continuation — DODO/USDT P55_89

**Symbol:** DODO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6979 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.5871 |
| sortino_ratio | -0.7233 |
| max_drawdown | 0.5904 |
| cagr | -0.2823 |
| net_avg_win | 71.5768 |
| net_avg_loss | -93.3702 |
| avg_hold_time_bars | 6.5052 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
