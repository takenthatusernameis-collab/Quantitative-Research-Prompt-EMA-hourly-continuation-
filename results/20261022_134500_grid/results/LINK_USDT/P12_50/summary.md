# EMA Hourly Continuation — LINK/USDT P12_50

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.6101 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 1.0672 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -6.7915 |
| sortino_ratio | -3.0204 |
| max_drawdown | 0.9782 |
| cagr | -0.7759 |
| net_avg_win | 32.3748 |
| net_avg_loss | -46.4696 |
| avg_hold_time_bars | 6.9120 |
| exposure | 0.3176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
