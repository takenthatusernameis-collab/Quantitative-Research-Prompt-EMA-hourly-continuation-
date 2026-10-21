# EMA Hourly Continuation — ARB/USDT P12_144

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.9758 |
| net_win_rate | 0.5371 |
| gross_profit_factor | 1.1491 |
| gross_win_rate | 0.5371 |
| sharpe_ratio | -0.0795 |
| sortino_ratio | -0.0193 |
| max_drawdown | 0.1419 |
| cagr | -0.0140 |
| net_avg_win | 92.2480 |
| net_avg_loss | -109.6891 |
| avg_hold_time_bars | 56.1378 |
| exposure | 0.7221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
