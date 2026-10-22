# EMA Hourly Continuation — MNT/USDT P12_144

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6481 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9673 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.3909 |
| sortino_ratio | -0.6591 |
| max_drawdown | 0.5774 |
| cagr | -0.2759 |
| net_avg_win | 53.2709 |
| net_avg_loss | -80.1123 |
| avg_hold_time_bars | 40.6324 |
| exposure | 0.7185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
