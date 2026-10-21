# EMA Hourly Continuation — CARV/USDT P100_200

**Symbol:** CARV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.6758 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8786 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -1.8607 |
| sortino_ratio | -0.4309 |
| max_drawdown | 0.3521 |
| cagr | -0.1797 |
| net_avg_win | 68.3006 |
| net_avg_loss | -90.3302 |
| avg_hold_time_bars | 15.0140 |
| exposure | 0.1808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
