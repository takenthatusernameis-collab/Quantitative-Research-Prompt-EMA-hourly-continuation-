# EMA Hourly Continuation — IOTA/USDT P50_200

**Symbol:** IOTA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7885 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9588 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -1.2245 |
| sortino_ratio | -0.2932 |
| max_drawdown | 0.3331 |
| cagr | -0.1272 |
| net_avg_win | 78.1861 |
| net_avg_loss | -95.6872 |
| avg_hold_time_bars | 30.1566 |
| exposure | 0.3852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
