# EMA Hourly Continuation — XEC/USDT P20_34

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6257 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9803 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -3.3570 |
| sortino_ratio | -1.0659 |
| max_drawdown | 0.7282 |
| cagr | -0.3840 |
| net_avg_win | 49.1345 |
| net_avg_loss | -75.9935 |
| avg_hold_time_bars | 5.3115 |
| exposure | 0.1173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
