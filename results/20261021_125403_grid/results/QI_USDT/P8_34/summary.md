# EMA Hourly Continuation — QI/USDT P8_34

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 817 |
| net_profit_factor | 0.7432 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 1.0079 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -2.8743 |
| sortino_ratio | -1.1753 |
| max_drawdown | 0.7488 |
| cagr | -0.4159 |
| net_avg_win | 52.7825 |
| net_avg_loss | -70.5028 |
| avg_hold_time_bars | 8.6903 |
| exposure | 0.3213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
