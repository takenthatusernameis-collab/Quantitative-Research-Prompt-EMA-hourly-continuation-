# EMA Hourly Continuation — CRV/USDT P8_144

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.6741 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -2.4486 |
| sortino_ratio | -0.6554 |
| max_drawdown | 0.5744 |
| cagr | -0.2687 |
| net_avg_win | 65.4496 |
| net_avg_loss | -87.8913 |
| avg_hold_time_bars | 49.1215 |
| exposure | 0.8083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
