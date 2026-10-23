# EMA Hourly Continuation — EUL/USDT P8_144

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6049 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8464 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -3.0901 |
| sortino_ratio | -0.9911 |
| max_drawdown | 0.7009 |
| cagr | -0.3749 |
| net_avg_win | 43.8189 |
| net_avg_loss | -62.8367 |
| avg_hold_time_bars | 29.9597 |
| exposure | 0.7095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
