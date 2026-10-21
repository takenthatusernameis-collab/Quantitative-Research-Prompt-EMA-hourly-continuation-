# EMA Hourly Continuation — CTC/USDT P89_144

**Symbol:** CTC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.6959 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.9677 |
| sortino_ratio | -0.4721 |
| max_drawdown | 0.4332 |
| cagr | -0.1948 |
| net_avg_win | 69.0785 |
| net_avg_loss | -98.5600 |
| avg_hold_time_bars | 7.2903 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
