# EMA Hourly Continuation — CPOOL/USDT P21_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 966 |
| net_profit_factor | 0.5640 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8241 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -5.8193 |
| sortino_ratio | -2.5160 |
| max_drawdown | 0.9576 |
| cagr | -0.7135 |
| net_avg_win | 27.9301 |
| net_avg_loss | -41.9497 |
| avg_hold_time_bars | 4.8747 |
| exposure | 0.2140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
