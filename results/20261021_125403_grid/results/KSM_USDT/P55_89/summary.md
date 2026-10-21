# EMA Hourly Continuation — KSM/USDT P55_89

**Symbol:** KSM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6613 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9346 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -2.3359 |
| sortino_ratio | -0.6053 |
| max_drawdown | 0.5225 |
| cagr | -0.2411 |
| net_avg_win | 61.7641 |
| net_avg_loss | -87.3209 |
| avg_hold_time_bars | 6.3792 |
| exposure | 0.0948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
