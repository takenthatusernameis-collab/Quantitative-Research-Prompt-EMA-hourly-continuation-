# EMA Hourly Continuation — DASH/USDT P12_26

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1397 |
| net_profit_factor | 0.1935 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.6031 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -11.7832 |
| sortino_ratio | -6.2148 |
| max_drawdown | 0.9997 |
| cagr | -0.9603 |
| net_avg_win | 4.0863 |
| net_avg_loss | -15.3032 |
| avg_hold_time_bars | 2.8418 |
| exposure | 0.1805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
