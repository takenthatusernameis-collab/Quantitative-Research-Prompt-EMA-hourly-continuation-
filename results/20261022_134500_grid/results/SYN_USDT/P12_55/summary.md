# EMA Hourly Continuation — SYN/USDT P12_55

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.6086 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9529 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -4.6724 |
| sortino_ratio | -2.0357 |
| max_drawdown | 0.9167 |
| cagr | -0.6267 |
| net_avg_win | 30.8894 |
| net_avg_loss | -46.2409 |
| avg_hold_time_bars | 9.3340 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
