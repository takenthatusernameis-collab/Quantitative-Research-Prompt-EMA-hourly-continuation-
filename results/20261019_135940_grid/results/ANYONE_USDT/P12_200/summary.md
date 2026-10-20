# EMA Hourly Continuation — ANYONE/USDT P12_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.8640 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0669 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -0.7559 |
| sortino_ratio | -0.1817 |
| max_drawdown | 0.2752 |
| cagr | -0.0842 |
| net_avg_win | 86.6846 |
| net_avg_loss | -106.8034 |
| avg_hold_time_bars | 60.7734 |
| exposure | 0.7862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
