# EMA Hourly Continuation — OGN/USDT P12_34

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6466 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9295 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -3.7090 |
| sortino_ratio | -1.3559 |
| max_drawdown | 0.7923 |
| cagr | -0.4636 |
| net_avg_win | 46.3190 |
| net_avg_loss | -65.3660 |
| avg_hold_time_bars | 7.0610 |
| exposure | 0.2096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
