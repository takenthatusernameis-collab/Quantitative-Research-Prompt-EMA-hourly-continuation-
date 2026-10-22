# EMA Hourly Continuation — MNT/USDT P8_200

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.7620 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0476 |
| gross_win_rate | 0.5199 |
| sharpe_ratio | -1.2548 |
| sortino_ratio | -0.3082 |
| max_drawdown | 0.3684 |
| cagr | -0.1379 |
| net_avg_win | 64.2644 |
| net_avg_loss | -88.9268 |
| avg_hold_time_bars | 61.1026 |
| exposure | 0.8388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
