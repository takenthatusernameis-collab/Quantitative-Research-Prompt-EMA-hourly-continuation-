# EMA Hourly Continuation — AURORA/USDT P20_200

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.6874 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.2404 |
| sortino_ratio | -0.5660 |
| max_drawdown | 0.5063 |
| cagr | -0.2300 |
| net_avg_win | 72.4943 |
| net_avg_loss | -90.0397 |
| avg_hold_time_bars | 39.4700 |
| exposure | 0.5687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
