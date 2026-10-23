# EMA Hourly Continuation — ORCA/USDT P12_20

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1331 |
| net_profit_factor | 0.4570 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.9821 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -9.9300 |
| sortino_ratio | -5.1066 |
| max_drawdown | 0.9986 |
| cagr | -0.9243 |
| net_avg_win | 14.1932 |
| net_avg_loss | -24.8810 |
| avg_hold_time_bars | 2.9331 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
