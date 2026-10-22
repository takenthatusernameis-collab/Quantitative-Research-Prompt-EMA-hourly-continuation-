# EMA Hourly Continuation — OP/USDT P55_89

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.4821 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8816 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -5.2265 |
| sortino_ratio | -1.9371 |
| max_drawdown | 0.9056 |
| cagr | -0.6028 |
| net_avg_win | 26.3896 |
| net_avg_loss | -47.8235 |
| avg_hold_time_bars | 3.6760 |
| exposure | 0.1140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
