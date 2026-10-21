# EMA Hourly Continuation — TRX/USDT P50_55

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 75 |
| net_profit_factor | 0.3819 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.1026 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -2.1769 |
| sortino_ratio | -0.2810 |
| max_drawdown | 0.2774 |
| cagr | -0.1173 |
| net_avg_win | 42.6083 |
| net_avg_loss | -120.8823 |
| avg_hold_time_bars | 6.4800 |
| exposure | 0.0221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
