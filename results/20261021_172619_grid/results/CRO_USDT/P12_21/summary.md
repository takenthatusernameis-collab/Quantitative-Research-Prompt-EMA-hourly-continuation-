# EMA Hourly Continuation — CRO/USDT P12_21

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.4902 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -3.7466 |
| sortino_ratio | -0.9626 |
| max_drawdown | 0.6772 |
| cagr | -0.3575 |
| net_avg_win | 44.7904 |
| net_avg_loss | -74.7617 |
| avg_hold_time_bars | 5.4531 |
| exposure | 0.0793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
