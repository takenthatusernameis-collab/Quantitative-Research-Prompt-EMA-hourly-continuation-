# EMA Hourly Continuation — COTI/USDT P34_55

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7194 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9443 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.7224 |
| sortino_ratio | -0.4035 |
| max_drawdown | 0.4147 |
| cagr | -0.1685 |
| net_avg_win | 73.1207 |
| net_avg_loss | -95.7527 |
| avg_hold_time_bars | 6.3396 |
| exposure | 0.0772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
