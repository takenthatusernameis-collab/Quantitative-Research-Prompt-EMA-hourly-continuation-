# EMA Hourly Continuation — XLM/USDT P26_55

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.3143 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -8.5053 |
| sortino_ratio | -3.6626 |
| max_drawdown | 0.9904 |
| cagr | -0.8416 |
| net_avg_win | 10.7824 |
| net_avg_loss | -28.3170 |
| avg_hold_time_bars | 4.3545 |
| exposure | 0.1843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
