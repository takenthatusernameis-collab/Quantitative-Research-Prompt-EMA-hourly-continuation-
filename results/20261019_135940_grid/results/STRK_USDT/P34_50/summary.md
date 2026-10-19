# EMA Hourly Continuation — STRK/USDT P34_50

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.4203 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -8.5055 |
| sortino_ratio | -3.6119 |
| max_drawdown | 0.9890 |
| cagr | -0.8326 |
| net_avg_win | 18.6666 |
| net_avg_loss | -33.5740 |
| avg_hold_time_bars | 2.4899 |
| exposure | 0.1010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
