# EMA Hourly Continuation — DEEP/USDT P89_144

**Symbol:** DEEP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.8308 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0152 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -0.8250 |
| sortino_ratio | -0.1826 |
| max_drawdown | 0.1686 |
| cagr | -0.0816 |
| net_avg_win | 79.8507 |
| net_avg_loss | -99.1769 |
| avg_hold_time_bars | 8.4241 |
| exposure | 0.0911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
