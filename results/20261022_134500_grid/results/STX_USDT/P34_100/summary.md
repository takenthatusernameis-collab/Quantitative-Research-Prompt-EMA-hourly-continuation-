# EMA Hourly Continuation — STX/USDT P34_100

**Symbol:** STX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -3.6148 |
| sortino_ratio | -1.2838 |
| max_drawdown | 0.7817 |
| cagr | -0.4530 |
| net_avg_win | 46.1201 |
| net_avg_loss | -66.5778 |
| avg_hold_time_bars | 8.6899 |
| exposure | 0.2485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
