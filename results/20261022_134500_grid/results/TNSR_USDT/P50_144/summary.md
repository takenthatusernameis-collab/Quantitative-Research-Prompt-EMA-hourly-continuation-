# EMA Hourly Continuation — TNSR/USDT P50_144

**Symbol:** TNSR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6176 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -3.6784 |
| sortino_ratio | -1.1927 |
| max_drawdown | 0.7605 |
| cagr | -0.4304 |
| net_avg_win | 50.8187 |
| net_avg_loss | -68.8517 |
| avg_hold_time_bars | 12.1758 |
| exposure | 0.2915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
