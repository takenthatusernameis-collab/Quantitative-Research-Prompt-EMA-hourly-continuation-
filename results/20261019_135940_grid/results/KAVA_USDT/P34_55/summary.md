# EMA Hourly Continuation — KAVA/USDT P34_55

**Symbol:** KAVA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 962 |
| net_profit_factor | 0.4051 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -10.8179 |
| sortino_ratio | -4.8202 |
| max_drawdown | 0.9981 |
| cagr | -0.9161 |
| net_avg_win | 17.7895 |
| net_avg_loss | -28.9237 |
| avg_hold_time_bars | 3.5104 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
