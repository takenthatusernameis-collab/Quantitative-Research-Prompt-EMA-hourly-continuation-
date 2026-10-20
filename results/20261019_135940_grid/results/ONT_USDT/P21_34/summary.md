# EMA Hourly Continuation — ONT/USDT P21_34

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.3478 |
| net_win_rate | 0.3933 |
| gross_profit_factor | 0.8037 |
| gross_win_rate | 0.4240 |
| sharpe_ratio | -11.4124 |
| sortino_ratio | -5.3239 |
| max_drawdown | 0.9991 |
| cagr | -0.9374 |
| net_avg_win | 12.6266 |
| net_avg_loss | -23.5318 |
| avg_hold_time_bars | 2.8388 |
| exposure | 0.1378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
