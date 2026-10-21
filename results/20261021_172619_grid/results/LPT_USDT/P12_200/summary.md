# EMA Hourly Continuation — LPT/USDT P12_200

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7417 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -1.6481 |
| sortino_ratio | -0.4208 |
| max_drawdown | 0.4487 |
| cagr | -0.1762 |
| net_avg_win | 72.8168 |
| net_avg_loss | -87.2643 |
| avg_hold_time_bars | 49.3406 |
| exposure | 0.7244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
