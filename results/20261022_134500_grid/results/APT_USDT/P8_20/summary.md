# EMA Hourly Continuation — APT/USDT P8_20

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1701 |
| net_profit_factor | 0.2843 |
| net_win_rate | 0.4080 |
| gross_profit_factor | 0.7274 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -13.6495 |
| sortino_ratio | -7.9481 |
| max_drawdown | 1.0000 |
| cagr | -0.9833 |
| net_avg_win | 5.7239 |
| net_avg_loss | -13.8749 |
| avg_hold_time_bars | 2.7078 |
| exposure | 0.2094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
