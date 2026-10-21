# EMA Hourly Continuation — XLM/USDT P20_34

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7629 |
| net_win_rate | 0.5374 |
| gross_profit_factor | 1.1627 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -1.4025 |
| sortino_ratio | -0.3406 |
| max_drawdown | 0.3495 |
| cagr | -0.1437 |
| net_avg_win | 68.7535 |
| net_avg_loss | -104.6827 |
| avg_hold_time_bars | 5.8577 |
| exposure | 0.0748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
