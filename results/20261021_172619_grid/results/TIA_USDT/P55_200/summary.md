# EMA Hourly Continuation — TIA/USDT P55_200

**Symbol:** TIA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.8231 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.0209 |
| sortino_ratio | -0.2382 |
| max_drawdown | 0.2874 |
| cagr | -0.1053 |
| net_avg_win | 86.5779 |
| net_avg_loss | -101.3156 |
| avg_hold_time_bars | 30.2172 |
| exposure | 0.3667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
