# EMA Hourly Continuation — TIA/USDT P21_26

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.7758 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0324 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -0.8897 |
| sortino_ratio | -0.1558 |
| max_drawdown | 0.2225 |
| cagr | -0.0690 |
| net_avg_win | 74.8356 |
| net_avg_loss | -101.8205 |
| avg_hold_time_bars | 4.2838 |
| exposure | 0.0288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
