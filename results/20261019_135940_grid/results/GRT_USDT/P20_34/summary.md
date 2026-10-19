# EMA Hourly Continuation — GRT/USDT P20_34

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1142 |
| net_profit_factor | 0.3743 |
| net_win_rate | 0.4124 |
| gross_profit_factor | 0.7878 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -10.6480 |
| sortino_ratio | -5.0979 |
| max_drawdown | 0.9985 |
| cagr | -0.9243 |
| net_avg_win | 12.6816 |
| net_avg_loss | -23.7826 |
| avg_hold_time_bars | 2.5508 |
| exposure | 0.1318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
