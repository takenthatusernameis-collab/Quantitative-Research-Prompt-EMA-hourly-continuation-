# EMA Hourly Continuation — ORBS/USDT P12_50

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1125 |
| net_profit_factor | 0.4750 |
| net_win_rate | 0.4178 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -9.1850 |
| sortino_ratio | -4.3380 |
| max_drawdown | 0.9955 |
| cagr | -0.8823 |
| net_avg_win | 19.1613 |
| net_avg_loss | -28.9456 |
| avg_hold_time_bars | 7.4302 |
| exposure | 0.3800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
