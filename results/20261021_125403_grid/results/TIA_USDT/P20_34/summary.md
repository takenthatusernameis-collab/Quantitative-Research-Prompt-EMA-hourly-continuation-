# EMA Hourly Continuation — TIA/USDT P20_34

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7989 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0469 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -1.0897 |
| sortino_ratio | -0.2783 |
| max_drawdown | 0.3840 |
| cagr | -0.1203 |
| net_avg_win | 67.1026 |
| net_avg_loss | -90.6679 |
| avg_hold_time_bars | 5.2580 |
| exposure | 0.0750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
