# EMA Hourly Continuation — MANTA/USDT P8_89

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 1.0286 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -3.7249 |
| sortino_ratio | -1.3752 |
| max_drawdown | 0.8154 |
| cagr | -0.4822 |
| net_avg_win | 61.8182 |
| net_avg_loss | -78.7350 |
| avg_hold_time_bars | 21.5826 |
| exposure | 0.6769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
