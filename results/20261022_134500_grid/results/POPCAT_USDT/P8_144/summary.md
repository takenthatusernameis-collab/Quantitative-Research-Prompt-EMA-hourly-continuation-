# EMA Hourly Continuation — POPCAT/USDT P8_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7191 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -2.5167 |
| sortino_ratio | -0.7909 |
| max_drawdown | 0.5781 |
| cagr | -0.3177 |
| net_avg_win | 68.8543 |
| net_avg_loss | -88.5542 |
| avg_hold_time_bars | 32.3126 |
| exposure | 0.7425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
