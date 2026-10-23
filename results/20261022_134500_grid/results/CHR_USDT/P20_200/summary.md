# EMA Hourly Continuation — CHR/USDT P20_200

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7520 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -1.5926 |
| sortino_ratio | -0.3862 |
| max_drawdown | 0.4286 |
| cagr | -0.1706 |
| net_avg_win | 76.5448 |
| net_avg_loss | -99.7814 |
| avg_hold_time_bars | 52.2857 |
| exposure | 0.7122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
