# EMA Hourly Continuation — XAI/USDT P26_200

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.9478 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.1001 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -0.2386 |
| sortino_ratio | -0.0535 |
| max_drawdown | 0.2941 |
| cagr | -0.0279 |
| net_avg_win | 97.9840 |
| net_avg_loss | -114.1722 |
| avg_hold_time_bars | 59.8884 |
| exposure | 0.6588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
