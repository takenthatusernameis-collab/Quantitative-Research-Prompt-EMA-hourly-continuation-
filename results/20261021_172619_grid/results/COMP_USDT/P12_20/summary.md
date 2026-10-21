# EMA Hourly Continuation — COMP/USDT P12_20

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.5155 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.8015 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -4.5850 |
| sortino_ratio | -1.3814 |
| max_drawdown | 0.8012 |
| cagr | -0.4712 |
| net_avg_win | 44.0029 |
| net_avg_loss | -66.6956 |
| avg_hold_time_bars | 4.4568 |
| exposure | 0.0891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
