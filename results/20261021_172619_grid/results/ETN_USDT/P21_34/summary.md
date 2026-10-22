# EMA Hourly Continuation — ETN/USDT P21_34

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.3879 |
| net_win_rate | 0.3396 |
| gross_profit_factor | 0.5189 |
| gross_win_rate | 0.3396 |
| sharpe_ratio | -5.2392 |
| sortino_ratio | -1.3185 |
| max_drawdown | 0.7328 |
| cagr | -0.4614 |
| net_avg_win | 51.2208 |
| net_avg_loss | -67.9177 |
| avg_hold_time_bars | 6.3585 |
| exposure | 0.0915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
