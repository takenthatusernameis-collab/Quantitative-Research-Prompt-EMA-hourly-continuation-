# EMA Hourly Continuation — ASTR/USDT P89_144

**Symbol:** ASTR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6114 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.8869 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -2.7192 |
| sortino_ratio | -0.7016 |
| max_drawdown | 0.5805 |
| cagr | -0.2767 |
| net_avg_win | 56.6753 |
| net_avg_loss | -84.0177 |
| avg_hold_time_bars | 8.5276 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
