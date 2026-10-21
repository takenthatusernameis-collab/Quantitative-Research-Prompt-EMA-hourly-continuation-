# EMA Hourly Continuation — LDO/USDT P34_144

**Symbol:** LDO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7141 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -2.1586 |
| sortino_ratio | -0.5897 |
| max_drawdown | 0.5209 |
| cagr | -0.2382 |
| net_avg_win | 72.7243 |
| net_avg_loss | -85.7093 |
| avg_hold_time_bars | 22.2016 |
| exposure | 0.3754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
