# EMA Hourly Continuation — POPCAT/USDT P8_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.9174 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0620 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -0.5703 |
| sortino_ratio | -0.1811 |
| max_drawdown | 0.3151 |
| cagr | -0.0855 |
| net_avg_win | 89.8841 |
| net_avg_loss | -104.7376 |
| avg_hold_time_bars | 28.8310 |
| exposure | 0.6397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
