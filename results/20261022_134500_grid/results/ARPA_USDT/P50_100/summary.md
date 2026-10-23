# EMA Hourly Continuation — ARPA/USDT P50_100

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4404 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.7731 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -6.9037 |
| sortino_ratio | -2.5660 |
| max_drawdown | 0.9606 |
| cagr | -0.7186 |
| net_avg_win | 25.3309 |
| net_avg_loss | -42.3216 |
| avg_hold_time_bars | 6.0498 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
