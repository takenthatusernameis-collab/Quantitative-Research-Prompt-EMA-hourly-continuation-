# EMA Hourly Continuation — PEPE/USDT P34_89

**Symbol:** PEPE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5707 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8849 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -5.3935 |
| sortino_ratio | -1.9607 |
| max_drawdown | 0.9186 |
| cagr | -0.6224 |
| net_avg_win | 39.2894 |
| net_avg_loss | -57.6524 |
| avg_hold_time_bars | 7.1357 |
| exposure | 0.2199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
