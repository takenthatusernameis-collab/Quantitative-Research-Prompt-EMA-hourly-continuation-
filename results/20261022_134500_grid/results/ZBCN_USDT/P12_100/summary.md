# EMA Hourly Continuation — ZBCN/USDT P12_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.6908 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9682 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -3.5608 |
| sortino_ratio | -1.4770 |
| max_drawdown | 0.8311 |
| cagr | -0.5082 |
| net_avg_win | 44.3887 |
| net_avg_loss | -60.6119 |
| avg_hold_time_bars | 12.9568 |
| exposure | 0.5137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
