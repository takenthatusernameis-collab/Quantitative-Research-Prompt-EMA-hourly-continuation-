# EMA Hourly Continuation — SHR/USDT P20_55

**Symbol:** SHR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1216 |
| net_profit_factor | 0.3966 |
| net_win_rate | 0.3183 |
| gross_profit_factor | 0.6060 |
| gross_win_rate | 0.3224 |
| sharpe_ratio | -11.7324 |
| sortino_ratio | -5.7236 |
| max_drawdown | 0.9991 |
| cagr | -0.9379 |
| net_avg_win | 16.9694 |
| net_avg_loss | -19.9736 |
| avg_hold_time_bars | 4.4350 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
