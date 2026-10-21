# EMA Hourly Continuation — ATH/USDT P100_200

**Symbol:** ATH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.8245 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0164 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -0.9807 |
| sortino_ratio | -0.2259 |
| max_drawdown | 0.2612 |
| cagr | -0.0996 |
| net_avg_win | 84.3028 |
| net_avg_loss | -103.9560 |
| avg_hold_time_bars | 14.5785 |
| exposure | 0.1710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
