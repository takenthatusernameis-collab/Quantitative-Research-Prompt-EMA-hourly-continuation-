# EMA Hourly Continuation — CYBER/USDT P34_200

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0670 |
| gross_win_rate | 0.5181 |
| sharpe_ratio | -1.4173 |
| sortino_ratio | -0.3819 |
| max_drawdown | 0.3949 |
| cagr | -0.1640 |
| net_avg_win | 68.7692 |
| net_avg_loss | -93.0052 |
| avg_hold_time_bars | 31.4345 |
| exposure | 0.5130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
