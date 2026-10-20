# EMA Hourly Continuation — KSM/USDT P89_144

**Symbol:** KSM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.5104 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -4.7963 |
| sortino_ratio | -1.5076 |
| max_drawdown | 0.8447 |
| cagr | -0.5217 |
| net_avg_win | 37.7221 |
| net_avg_loss | -65.7274 |
| avg_hold_time_bars | 4.6970 |
| exposure | 0.1057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
