# EMA Hourly Continuation — CKB/USDT P50_144

**Symbol:** CKB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5385 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8120 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -4.2931 |
| sortino_ratio | -1.3728 |
| max_drawdown | 0.8199 |
| cagr | -0.4871 |
| net_avg_win | 40.1924 |
| net_avg_loss | -62.0253 |
| avg_hold_time_bars | 11.2231 |
| exposure | 0.2653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
