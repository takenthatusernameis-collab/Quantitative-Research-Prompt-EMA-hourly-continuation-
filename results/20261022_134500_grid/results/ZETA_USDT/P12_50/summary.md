# EMA Hourly Continuation — ZETA/USDT P12_50

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1028 |
| net_profit_factor | 0.6003 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -6.2724 |
| sortino_ratio | -2.8218 |
| max_drawdown | 0.9679 |
| cagr | -0.7432 |
| net_avg_win | 31.1231 |
| net_avg_loss | -43.1558 |
| avg_hold_time_bars | 8.0837 |
| exposure | 0.3760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
