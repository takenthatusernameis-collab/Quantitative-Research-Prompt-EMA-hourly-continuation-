# EMA Hourly Continuation — AVAX/USDT P12_34

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.6763 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -3.5180 |
| sortino_ratio | -1.1854 |
| max_drawdown | 0.7652 |
| cagr | -0.4197 |
| net_avg_win | 60.8128 |
| net_avg_loss | -76.2193 |
| avg_hold_time_bars | 6.6237 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
