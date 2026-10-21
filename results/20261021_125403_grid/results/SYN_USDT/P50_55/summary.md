# EMA Hourly Continuation — SYN/USDT P50_55

**Symbol:** SYN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.5725 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8156 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -2.2909 |
| sortino_ratio | -0.4363 |
| max_drawdown | 0.4045 |
| cagr | -0.1806 |
| net_avg_win | 65.8812 |
| net_avg_loss | -93.9406 |
| avg_hold_time_bars | 5.3090 |
| exposure | 0.0430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
