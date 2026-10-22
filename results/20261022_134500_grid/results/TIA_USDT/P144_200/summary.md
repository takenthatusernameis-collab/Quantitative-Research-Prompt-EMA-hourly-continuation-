# EMA Hourly Continuation — TIA/USDT P144_200

**Symbol:** TIA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.5653 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.9136 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -3.6854 |
| sortino_ratio | -1.0006 |
| max_drawdown | 0.7071 |
| cagr | -0.3798 |
| net_avg_win | 53.1265 |
| net_avg_loss | -81.9985 |
| avg_hold_time_bars | 4.4251 |
| exposure | 0.0738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
