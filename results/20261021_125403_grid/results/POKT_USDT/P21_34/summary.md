# EMA Hourly Continuation — POKT/USDT P21_34

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.4891 |
| net_win_rate | 0.3723 |
| gross_profit_factor | 0.6824 |
| gross_win_rate | 0.3771 |
| sharpe_ratio | -5.1866 |
| sortino_ratio | -1.4845 |
| max_drawdown | 0.8270 |
| cagr | -0.4986 |
| net_avg_win | 51.6129 |
| net_avg_loss | -62.5742 |
| avg_hold_time_bars | 6.2141 |
| exposure | 0.1156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
