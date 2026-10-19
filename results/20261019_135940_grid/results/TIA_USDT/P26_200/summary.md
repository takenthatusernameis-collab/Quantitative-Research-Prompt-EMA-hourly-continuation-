# EMA Hourly Continuation — TIA/USDT P26_200

**Symbol:** TIA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8081 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0139 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.1107 |
| sortino_ratio | -0.2759 |
| max_drawdown | 0.3059 |
| cagr | -0.1206 |
| net_avg_win | 76.3930 |
| net_avg_loss | -95.7943 |
| avg_hold_time_bars | 45.4371 |
| exposure | 0.6237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
