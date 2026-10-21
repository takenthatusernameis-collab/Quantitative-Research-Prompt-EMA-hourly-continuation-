# EMA Hourly Continuation — RUNE/USDT P8_55

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.8009 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0218 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.9026 |
| sortino_ratio | -0.6958 |
| max_drawdown | 0.5772 |
| cagr | -0.2748 |
| net_avg_win | 67.6890 |
| net_avg_loss | -86.0911 |
| avg_hold_time_bars | 15.4801 |
| exposure | 0.4588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
