# EMA Hourly Continuation — DBR/USDT P55_89

**Symbol:** DBR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.4199 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -6.8420 |
| sortino_ratio | -2.2683 |
| max_drawdown | 0.9076 |
| cagr | -0.6835 |
| net_avg_win | 35.6319 |
| net_avg_loss | -59.7210 |
| avg_hold_time_bars | 5.7111 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
