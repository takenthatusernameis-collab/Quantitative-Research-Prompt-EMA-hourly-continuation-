# EMA Hourly Continuation — MANTA/USDT P20_200

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.9154 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0532 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -0.4142 |
| sortino_ratio | -0.0922 |
| max_drawdown | 0.2108 |
| cagr | -0.0441 |
| net_avg_win | 94.2634 |
| net_avg_loss | -108.2586 |
| avg_hold_time_bars | 63.3375 |
| exposure | 0.6910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
