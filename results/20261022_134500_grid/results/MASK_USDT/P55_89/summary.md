# EMA Hourly Continuation — MASK/USDT P55_89

**Symbol:** MASK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.3413 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.7466 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -8.1455 |
| sortino_ratio | -3.0859 |
| max_drawdown | 0.9810 |
| cagr | -0.7931 |
| net_avg_win | 16.8866 |
| net_avg_loss | -35.9697 |
| avg_hold_time_bars | 4.1566 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
