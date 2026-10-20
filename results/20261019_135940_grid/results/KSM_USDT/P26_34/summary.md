# EMA Hourly Continuation — KSM/USDT P26_34

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.2615 |
| net_win_rate | 0.3693 |
| gross_profit_factor | 0.7998 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -12.6966 |
| sortino_ratio | -6.0735 |
| max_drawdown | 0.9996 |
| cagr | -0.9548 |
| net_avg_win | 8.9145 |
| net_avg_loss | -19.9629 |
| avg_hold_time_bars | 2.2716 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
