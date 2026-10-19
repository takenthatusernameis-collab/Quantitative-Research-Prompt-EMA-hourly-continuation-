# EMA Hourly Continuation — TIA/USDT P50_55

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 762 |
| net_profit_factor | 0.3233 |
| net_win_rate | 0.3937 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.4344 |
| sharpe_ratio | -9.8638 |
| sortino_ratio | -3.9172 |
| max_drawdown | 0.9944 |
| cagr | -0.8727 |
| net_avg_win | 15.8372 |
| net_avg_loss | -31.8066 |
| avg_hold_time_bars | 2.1430 |
| exposure | 0.0742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
