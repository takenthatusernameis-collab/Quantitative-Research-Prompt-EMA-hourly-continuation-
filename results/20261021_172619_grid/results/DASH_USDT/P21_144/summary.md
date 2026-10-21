# EMA Hourly Continuation — DASH/USDT P21_144

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7105 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.8818 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -2.0042 |
| sortino_ratio | -0.5307 |
| max_drawdown | 0.4851 |
| cagr | -0.2174 |
| net_avg_win | 69.6451 |
| net_avg_loss | -85.8313 |
| avg_hold_time_bars | 32.7781 |
| exposure | 0.5170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
