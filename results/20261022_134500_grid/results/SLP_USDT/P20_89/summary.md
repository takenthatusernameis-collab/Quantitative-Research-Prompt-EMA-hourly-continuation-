# EMA Hourly Continuation — SLP/USDT P20_89

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 817 |
| net_profit_factor | 0.6245 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -5.5445 |
| sortino_ratio | -2.2240 |
| max_drawdown | 0.9353 |
| cagr | -0.6601 |
| net_avg_win | 41.9590 |
| net_avg_loss | -55.6137 |
| avg_hold_time_bars | 11.1591 |
| exposure | 0.4144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
