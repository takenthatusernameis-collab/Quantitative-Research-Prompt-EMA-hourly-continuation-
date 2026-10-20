# EMA Hourly Continuation — BIGTIME/USDT P8_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8850 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1160 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -0.5961 |
| sortino_ratio | -0.1430 |
| max_drawdown | 0.2841 |
| cagr | -0.0666 |
| net_avg_win | 82.9504 |
| net_avg_loss | -104.2997 |
| avg_hold_time_bars | 66.3060 |
| exposure | 0.8432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
