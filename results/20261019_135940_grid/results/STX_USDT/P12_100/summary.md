# EMA Hourly Continuation — STX/USDT P12_100

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -3.7162 |
| sortino_ratio | -1.2909 |
| max_drawdown | 0.8146 |
| cagr | -0.4579 |
| net_avg_win | 45.6495 |
| net_avg_loss | -64.5140 |
| avg_hold_time_bars | 22.4118 |
| exposure | 0.6207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
