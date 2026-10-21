# EMA Hourly Continuation — CKB/USDT P8_26

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.6925 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9304 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -3.5016 |
| sortino_ratio | -1.3815 |
| max_drawdown | 0.7977 |
| cagr | -0.4680 |
| net_avg_win | 49.0461 |
| net_avg_loss | -65.2841 |
| avg_hold_time_bars | 6.6124 |
| exposure | 0.2287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
