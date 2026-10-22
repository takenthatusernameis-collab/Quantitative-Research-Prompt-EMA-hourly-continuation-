# EMA Hourly Continuation — AVAX/USDT P12_26

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1380 |
| net_profit_factor | 0.4071 |
| net_win_rate | 0.4152 |
| gross_profit_factor | 0.9373 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -12.0129 |
| sortino_ratio | -6.3451 |
| max_drawdown | 0.9997 |
| cagr | -0.9604 |
| net_avg_win | 11.9770 |
| net_avg_loss | -20.8920 |
| avg_hold_time_bars | 2.8159 |
| exposure | 0.1766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
